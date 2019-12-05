from django.urls import path
from staff import views

app_name = 'staff'

urlpatterns = [
    # 공지사항
    path('board/', views.PostLV.as_view(), name='board_list'),
    # path('board/<int:pk>', views.post_detail, name='board_detail'),
    # path('board/<int:pk>', views.PostDV.as_view(), name='board_detail'),
    path('board/<int:pk>', views.post_ip, name='board_detail'),
    path('board/<int:pk>/edit/', views.post_edit, name='board_edit'),
    path('board/<int:pk>/remove/', views.post_remove, name='board_remove'),
    path('board/category/<int:pk>', views.post_filter, name='board_filter'),
    # QnA
    path('qna/', views.qnaView, name='qna'),
    path('qna/new', views.q_new, name='q_new'),
    path('qna/<int:pk>/remove/', views.qna_remove, name='qna_remove'),
    path('qna/<int:pk>/q_edit/', views.q_edit, name='q_edit'),
    path('qna/<int:pk>/a_edit/', views.a_edit, name='a_edit'),
    # 기부단체  # 7.18 소이 - 수정
    path('donation/', views.DonationLV.as_view(), name='donation'),
    # 응모권 # 190820 예림 수정
    path('ticket/<int:pk>', views.ticket, name='ticket'),
]