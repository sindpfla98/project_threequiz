from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
app_name = 'user'

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    re_path(r'^(?P<pk>\d+)/verify/(?P<token>[0-9A-Za-z]{1,3}-[0-9A-Za-z]{1,20})/$', views.UserVerificationView.as_view()),
    path('resend_verify_email/', views.ResendVerifyEmailView.as_view(), name='resend_verify_email'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('mail_cnf/', views.UserEmailView.as_view(), name='mail_cnf'),
    path('logout/', LogoutView.as_view(template_name='user/logged_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name='user/password_change_form.html', success_url=reverse_lazy('user:password_change_done')), name='password_change'),
    path('password_change/done', PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'), name='password_change_done'),
    # 190705 예림
    # path('mypage/', views.mypage, name='mypage'),
    # 190721 시인
    path('mypage/<int:pk>/', views.mypage, name='mypage'),
    path('rankinfo/', views.Rankinfo.as_view(), name='rankinfo'),
]