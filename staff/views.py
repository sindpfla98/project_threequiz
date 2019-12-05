from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from staff.models import *
from .forms import *
from django.shortcuts import redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # 6.2소이 - 페이지네이션
from ipaddr import client_ip  # 6.4 소이 - ip조회수


# 기부단체 목록
# 7.18 소이 - 변경
class DonationLV(ListView):
    model = DonationOrg
    template_name = "staff/donationOrg.html"
    context_object_name = 'donations'
    donations = DonationOrg.objects.all()


# 공지사항 목록
class PostLV(ListView):
    model = Board
    template_name = "staff/board_list.html"
    context_object_name = 'posts'
    paginate_by = 5
    posts = Board.objects.all()

    # 카테고리 목록 추가
    def get_context_data(self, **kwargs):
        context = super(PostLV, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


# 공지사항 상세
# class PostDV(DetailView):
#     model = Board
#     template_name = "staff/board_detail.html"
#     paginate_by = 2
#     context_object_name = 'post'

# ip주소 조회수
def post_ip(request, pk):
    post = get_object_or_404(Board, pk=pk)
    # posts = Board.objects.all()
    ip = client_ip(request)

    try:
        # ip주소와 게시글 번호로 기록을 조회함
        hits = HitCount.objects.get(ip=ip, post=post)
    except Exception as e:
        # 처음 게시글을 조회한 경우엔 조회 기록이 없음
        print(e)
        hits = HitCount.objects.create(ip=ip, post_id=post.id)
        Board.objects.filter(pk=pk).update(hits=post.hits + 1)
        hits.save()
        # 상세화면에서 조회수가 바로 바뀌지 않아서 강제로 출력 조회수 +1 시킴
        post.hits = post.hits + 1
    else:
        # 조회 기록은 있으나, 날짜가 다른 경우
        if not hits.date == timezone.now().date():
        # 테스트할 때 사용
        # if not hits.date == timezone.now():
            Board.objects.filter(pk=pk).update(hits=post.hits + 1)
            hits.date = timezone.now()
            hits.save()
            post.hits = post.hits+1
        # 날짜가 같은 경우
        else:
            print(str(ip) + ' has already hit this post.\n\n')
    return render(request, 'staff/board_detail.html', {'post': post})


# def post_detail(request, pk):
#     post = get_object_or_404(Board, pk=pk)
#     return render(request, 'staff/board_detail.html',{'post':post})

# 공지사항 수정
def post_edit(request, pk):
    post = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('staff:board_detail', pk=post.pk)
    else:
        form = BoardForm(instance=post)
    return render(request, 'staff/board_edit.html', {'form': form})


# 공지사항 삭제
def post_remove(request, pk):
    post = get_object_or_404(Board, pk=pk)
    post.delete()
    return redirect('staff:board_list')


# 카테고리 필터링
def post_filter(request, pk):
    posts = Board.objects.filter(category_id=pk)
    categories = Category.objects.all()
    return render(request, 'staff/board_list.html', {'posts': posts, 'categories': categories})


# QnA 두번째 게시판
def qnaView(request):
    advertisings = Advertising.objects.all().order_by('?')
    advertising1 = advertisings[0]
    advertising2 = advertisings[1]
    qnas = QnA.objects.all()
    # 6.2 소이 - 페이지네이션
    paginator = Paginator(qnas, 5)

    page = request.GET.get('page')
    try:
        qnas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        qnas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        qnas = paginator.page(paginator.num_pages)

    return render(request, 'staff/QnA.html', {'qnas': qnas, 'advertising1':advertising1, 'advertising2':advertising2})


# QnA 삭제
def qna_remove(request, pk):
    qna = get_object_or_404(QnA, pk=pk)
    qna.delete()
    return redirect('staff:qna')


# 질문 수정
def q_edit(request, pk):
    qna = get_object_or_404(QnA, pk=pk)
    if request.method == "POST":
        form = QForm(request.POST, instance=qna)
        if form.is_valid():
            qna = form.save(commit=False)
            qna.user = request.user
            qna.save()
            return redirect('staff:qna')
    else:
        form = QForm(instance=qna)
    return render(request, 'staff/QnA.html', {'qform': form})


# 답변 수정
def a_edit(request, pk):
    qna = get_object_or_404(QnA, pk=pk)
    if request.method == "POST":
        form = AForm(request.POST, instance=qna)
        if form.is_valid():
            qna = form.save(commit=False)
            qna.user = request.user
            qna.save()
            return redirect('staff:qna')
    else:
        form = AForm(instance=qna)
    return render(request, 'staff/QnA.html', {'aform': form})


# 질문쓰기
def q_new(request):
    if request.method == "POST":
        form = QForm(request.POST)
        if form.is_valid():
            qna = form.save(commit=False)
            qna.user = request.user
            qna.date = timezone.now()
            qna.save()
            return redirect('staff:qna')
    else:
        form = QForm()
    return render(request, 'staff/QnA.html', {'qform': form})


# 응모권 190820 예림
def ticket(request, pk):
    advertisings = Advertising.objects.all().order_by('?')
    advertising1 = advertisings[0]
    advertising2 = advertisings[1]
    tickets = Ticket.objects.all()
    user = User.objects.get(id=pk)
    user_ticket = user.ticket
    if request.method == "POST" and 'ticketing' in request.POST:
        user.ticket = user.ticket-1
        user.ticketing = user.ticketing+1
        user.save()
        return redirect('staff:ticket', pk=pk)
    return render(request, 'staff/ticket.html', {'tickets':tickets, 'user_ticket':user_ticket, 'pk':pk,
                                                 'advertising1':advertising1, 'advertising2':advertising2})

