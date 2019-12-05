from django.urls import path
from plant import views

app_name = 'plant'

urlpatterns = [
    # 0802 예림 - 작물 게임
    path('<int:pk>/',views.plantgame, name='userplant'),
    # 씨앗 선택
    path('selectSeed/<int:pk>/',views.selectSeed, name='selectSeed'),
    # 마이페이지 - 작물일지
    path('jakmulDiary/<int:pk>/', views.my_diaryview, name='jakmulDiary'),
    # 씨앗 정보
    path('seedinfo/',views.seedinfo.as_view(), name='seedinfo'),
    # 7.20 소이 - 기부단체선택
    path('org_select/<int:uk>/', views.org_select, name='org_select'),
    # 7.21 소이 - 배송확인
    path('delivery/<int:uk>/', views.delivery_profile, name='delivery'),
]
