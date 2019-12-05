from django import forms
from .models import *
from django.contrib.auth import get_user_model

class PlantForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['exp']

# 8.19 소이 - 추가
# 배송확인페이지
class profileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['name', 'postcode', 'address', 'detail_address', 'ref_address', 'phone', ]

        


