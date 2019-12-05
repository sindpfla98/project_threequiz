from django.shortcuts import render
from django.views.generic import TemplateView
from quiz.models import *
from user.models import Item, HaveItem, User
from django.shortcuts import redirect
from staff.models import Advertising
import datetime

# 퀴즈 주제 190709 예림: 숫자 반복적으로 쓰지 않고도 될수있게 수정하기.
def q_sub(request, uk):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    advertisings = Advertising.objects.all().order_by('?')
    advertising1 = advertisings[0]
    advertising2 = advertisings[1]
    if len(MyQuiz.objects.filter(user_id=uk, date=today)) <= 5 and len(MyQuiz.objects.filter(user_id=uk, date=today)) > 0:
        quiz_num = MyQuiz.objects.filter(user_id=uk, date=today).last().quiz_id
        quizSubs = QuizSub.objects.get(id=Quiz.objects.get(id=quiz_num).quizSub_id)
        return redirect('quiz:quiz_real', pk=quizSubs.id, uk=uk)
    elif len(MyQuiz.objects.filter(user_id=uk, date=today)) > 5:
        quiz_num = MyQuiz.objects.filter(user_id=uk, date=today).last().quiz_id
        quizSubs = QuizSub.objects.get(id=Quiz.objects.get(id=quiz_num).quizSub_id)
        count = 0
        item = Item.objects.get(id=quizSubs.item_id)
        for i in MyQuiz.objects.filter(user_id=uk, date=today):
            if i.myAnswer == Quiz.objects.get(id=i.quiz_id).answer:
                count += 1
            else:
                continue
        return render(request, 'quiz/quiz_finish.html',
                          {'uk': uk, 'quizSubs': quizSubs.id, 'date': today, 'count': count, 'qnum': 10, 'item': item})
    else:
        quizSubs = QuizSub.objects.all()
        if request.method == "POST" and 'q_sub1' in request.POST:
            quizSubs = QuizSub.objects.get(id=1)
            return redirect('quiz:quiz_real', pk=quizSubs.pk, uk=uk)
        elif request.method == "POST" and 'q_sub2' in request.POST:
            quizSubs = QuizSub.objects.get(id=2)
            return redirect('quiz:quiz_real', pk=quizSubs.pk, uk=uk)
        elif request.method == "POST" and 'q_sub3' in request.POST:
            quizSubs = QuizSub.objects.get(id=3)
            return redirect('quiz:quiz_real', pk=quizSubs.pk, uk=uk)
        elif request.method == "POST" and 'q_sub4' in request.POST:
            quizSubs = QuizSub.objects.get(id=4)
            return redirect('quiz:quiz_real', pk=quizSubs.pk, uk=uk)
        elif request.method == "POST" and 'q_sub5' in request.POST:
            quizSubs = QuizSub.objects.get(id=5)
            return redirect('quiz:quiz_real', pk=quizSubs.pk, uk=uk)
    return render(request, 'quiz/quiz_sub.html', {'quizSubs': quizSubs, 'advertising1':advertising1, 'advertising2':advertising2})


# 문제푸는 화면
def quiz_real(request, pk, uk):
    quizSubs = QuizSub.objects.get(id=pk)
    # 퀴즈 주제에 맞는 문제
    quizs = Quiz.objects.filter(quizSub_id=pk)
    # 문제 맞춘 개수 출력 함수
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    myquizs = MyQuiz.objects.filter(user_id=uk, date=today)
    
    if not myquizs:
        qnum = 1
    elif myquizs.last().myAnswer == 'N':
        qnum = len(myquizs)
    else:
        qnum = len(myquizs)+1
    # 맞춘 문제 개수
    count=0
    # 오늘 회원이 푼 문제
    for myquiz in myquizs:
        # 회원답 정답 비교해서 같으면 +1
        if myquiz.myAnswer == Quiz.objects.get(id=myquiz.quiz_id).answer:
            count += 1

    # 회원이 처음으로 퀴즈를 풀거나 이전 퀴즈를 풀었다면
    # 마지막 줄에 답이 null이냐 아니냐로 if문 작성 못해서
    # 기본값으로 N을 넣고 이냐 아니냐를 판별
    def diffi():
        user_year = str(User.objects.get(id=uk).birth).split('-')[0]
        print(user_year)
        year = datetime.datetime.now().strftime('%Y')
        if int(year) - int(user_year) <= 8:
            diff = 1
        elif int(year) - int(user_year) <= 18:
            diff = 2
        else:
            diff = 3
        return diff
    if not myquizs or myquizs.last().myAnswer != "N":
        def exclude_quiz():
            user_quiz_all = MyQuiz.objects.filter(user_id=uk).exclude(myAnswer="N")

            # 랜덤으로 첫번째문제/다음문제 뽑기
            content = quizs.filter(difficulty=diffi()).order_by('?').first()
            if user_quiz_all.filter(quiz_id=content.id):
                if content.answer == user_quiz_all.filter(quiz_id=content.id).last().myAnswer:
                    return exclude_quiz()
            return content
        content = exclude_quiz()
        # 회원문제 테이블에 저장
        user_quiz_id = MyQuiz(myAnswer='N', quiz_id=content.id, user_id=uk)
        user_quiz_id.save()
    else:
        content = Quiz.objects.get(id=myquizs.last().quiz_id)
    # 문제의 답
    # answer = content.answer
    answer = Quiz.objects.get(id=myquizs.last().quiz_id).answer

    # O 버튼 눌렀을 때
    if request.method == "POST" and 'O' in request.POST:
        user_answer = myquizs.last()
        user_answer.myAnswer='O'
        user_answer.save()
        user_answer = myquizs.last().myAnswer
        if answer == user_answer:
            return render(request, 'quiz/right.html', {'quizSubs': quizSubs, 'count': count+1, 'qnum':qnum})
        # 틀렸을 때
        else:
            return render(request, 'quiz/wrong.html', {'quizSubs': quizSubs, 'count': count, 'qnum':qnum})
            # 오늘 풀 수 있는 문제 개수 및 다 풀었을 때

    # X 버튼 눌렀을 때
    elif request.method == "POST" and 'X' in request.POST:
        user_answer = MyQuiz.objects.filter(user_id=uk).last()
        user_answer.myAnswer="X"
        user_answer.save()

    # 정답 비교
        user_answer = MyQuiz.objects.filter(user_id=uk).last().myAnswer
        if answer == user_answer:
            return render(request, 'quiz/right.html', {'quizSubs': quizSubs, 'count': count+1, 'qnum':qnum})
        # 틀렸을 때
        else:
            return render(request, 'quiz/wrong.html', {'quizSubs': quizSubs, 'count': count, 'qnum':qnum})
        # return redirect('quiz:quiz_real', {'answer': answer})
    if request.method == "POST" and 'next' in request.POST:
        if MyQuiz.objects.filter(user_id=uk, date=today).count() > 5:
            date = MyQuiz.objects.filter(user_id=uk).last().date
            print("오늘 문제를 모두 풀었습니다.")
            item = Item.objects.get(id=quizSubs.item_id)
            try:
                user_item = HaveItem.objects.get(user_id=uk, item_id=quizSubs.item_id)
                user_item.item_count += count
                user_item.save()
            except HaveItem.DoesNotExist:
                user_item = HaveItem.objects.create(item_count=count, item_id=quizSubs.item_id, user_id=uk)
                user_item.save()
            return render(request, 'quiz/quiz_finish.html',
                          {'uk': uk, 'quizSubs': quizSubs, 'date': date, 'count': count, 'qnum': qnum, 'item': item})
        else:
            pass
    return render(request, 'quiz/quiz_real.html', {'quizs': content, 'quizSubs': quizSubs, 'count': count, 'qnum':qnum})

def quizinfo(request):
    quizinfos=[] # a 담을 리스트
    for i in QuizSub.objects.all():
        a = []  # 주제-도구
        quizSub = QuizSub.objects.get(id=i.id)
        a.append(quizSub)
        a.append(Item.objects.get(id=quizSub.item_id))
        quizinfos.append(a)
    return render(request, 'quiz/quizinfo.html', {'quizinfos':quizinfos})