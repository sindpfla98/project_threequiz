from django.contrib import admin
from .models import QuizSub, Quiz, MyQuiz, QuizCorrect
import operator

@admin.register(QuizSub)
class QuizSubAdmin(admin.ModelAdmin):
    list_display =['id', 'name', 'item', ]  # 8.20 소이 - 추가
    list_display_links = ['id', 'name', 'item', ]  # 8.20 소이 - 추가
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'quizSub', 'short_content', 'answer',
                    ]
    list_display_links = ['id', 'quizSub', 'short_content', ]
@admin.register(MyQuiz)
class MyQuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'quiz', 'date', 'myAnswer',
                    ]
    list_display_links = ['id', 'user', 'quiz', ]

# 190921
from django.shortcuts import render
@admin.register(QuizCorrect)
class QuizCorrectAdmin(admin.ModelAdmin):
    change_list_template = 'admin/quiz_correct_change_list.html'
    # list_filter = ('quizSub_id',)
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset.order_by('id')
        except (AttributeError, KeyError):
            return response
        def myquiz_correct(i):
            myquizs = MyQuiz.objects.filter(quiz_id=i)
            answer = Quiz.objects.get(id=i).answer
            correct = 0
            for myquiz in myquizs:
                if myquiz.myAnswer == answer:
                    correct = correct+1
            return correct
        def quiz_correct():
            correct_lst = []
            for i in Quiz.objects.all():
                correct_count = myquiz_correct(i.id)
                quiz_count = MyQuiz.objects.filter(quiz_id=i.id).count()
                if quiz_count != 0:
                    correct_lst.append(round(correct_count/quiz_count*100, 2))
                else:
                    correct_lst.append(0)
            return correct_lst

        qs_lst = {}
        for i in range(0, Quiz.objects.all().count()):
            qs_lst[qs[i]] = quiz_correct()[i]

        response.context_data['qs_lst'] = sorted(qs_lst.items(), key=operator.itemgetter(1), reverse=True)

        return response
