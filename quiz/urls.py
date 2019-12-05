from django.urls import path
from quiz import views

app_name = 'quiz'

urlpatterns = [
    path('quiz_subs/<int:uk>/', views.q_sub, name='quizSubs'),
    path('quiz_real/<int:uk>/<int:pk>/', views.quiz_real, name='quiz_real'),
    # path('right/', views.Right.as_view(), name='right'),
    # path('wrong/', views.Wrong.as_view(), name='wrong'),
    path('quizinfo/', views.quizinfo, name='quizinfo'),
]
