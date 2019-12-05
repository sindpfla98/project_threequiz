from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

from user.models import User


# 필터 기능을 위해 추가 --------------------------------------------------------------------------------
# class MyModelManager(models.Manager):
#     def get_queryset(self):
#         return super(MyModelManager, self).get_queryset().filter(category_id=2)

# 공지사항 분류
class Category(models.Model):
    name = models.CharField('분류', max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '분류'
        verbose_name_plural = '게시판 분류'


# 공지사항
class Board(models.Model):  # 게시판(댓글 기능 없는 공지사항 게시용)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='boards',
                             verbose_name='게시자')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='분류')
    title = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
    date = models.DateTimeField('작성일시', auto_now_add=True)
    hits = models.IntegerField('조회수', default=0)

    # 필터 기능을 위해 추가 --------------------------------------------------------------------------------
    # objects = MyModelManager()

    def short_content(self):  # 속성으로 존재하는 것처럼 만들기
        if self.content:
            t = self.content[:20] + '...'
        else:
            t = '(내용 없음)'
        return t

    short_content.short_description = '간략 내용'

    def get_absolute_url(self):
        return reverse('staff:board_detail', args=(self.id,))

    def get_newer_board(self):
        newer_board = Board.objects.filter(
            date__gt=self.date
        ).order_by('date').first()
        return newer_board

    def get_older_board(self):
        older_board = Board.objects.filter(
            date__lt=self.date
        ).order_by('-date').first()
        return older_board

    # # 조회수
    # @property
    # def update_counter(self):
    #     return self.hits

    class Meta:
        verbose_name = '게시판'
        verbose_name_plural = '관리자 게시판'
        ordering = ['-date']


# 두번째 게시판
class QnA(models.Model):
    user = models.ForeignKey(User, verbose_name='질문자', on_delete=models.CASCADE)
    title = models.CharField('제목', max_length=30)
    question = models.TextField('질문')
    lock = models.BooleanField('비공개', default=False)
    answer = models.TextField('답변', null=True)
    date = models.DateTimeField('작성일시', auto_now_add=True)

    class Meta:
        verbose_name = '질문'
        verbose_name_plural = '질문 게시판'
        ordering = ['-date']


# 기부단체 # 7.18 소이 - 전화번호 필드 추가
class DonationOrg(models.Model):
    name = models.CharField('기부단체명', max_length=20)
    desc = models.TextField('단체설명')
    photo = models.ImageField('사진', upload_to='staff/donation/')
    url = models.URLField('홈페이지 주소', max_length=250)
    phone = models.CharField('전화번호', max_length=20, blank=True, null=True)
    is_donate = models.BooleanField('이달 기부단체', default=False)

    def short_desc(self):
        if self.desc:
            t = self.desc[:20] + '...'
        else:
            t = '(내용 없음)'
        return t

    short_desc.short_description = '간략 단체설명'

    class Meta:
        verbose_name = '기부단체'
        verbose_name_plural = '기부단체'


# 조회수
class HitCount(models.Model):
    ip = models.CharField(max_length=15, default=None, null=True)  # ip 주소
    post = models.ForeignKey(Board, default=None, null=True, on_delete=models.CASCADE)  # 게시글
    date = models.DateField(auto_now_add=True, null=True, blank=True)  # 조회수가 올라갔던 날짜


# 응모권추첨
class Ticket(models.Model):
    name = models.CharField('경품이름', max_length=30)
    photo = models.ImageField(upload_to='staff/ticket', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "응모권"
        verbose_name = "응모권"

class Advertising(models.Model):
    name = models.CharField('기업 이름', max_length=50)
    url = models.URLField('홈페이지 주소')
    photo = models.ImageField(upload_to='staff/advertising')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "광고"
        verbose_name = "광고"

class DonationOrgSelect(DonationOrg):
    class Meta:
        proxy = True
        verbose_name = '기부단체 선택률'
        verbose_name_plural = '기부단체 선택률'