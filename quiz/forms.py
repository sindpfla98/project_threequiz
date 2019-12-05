from django import forms
from .models import *

# class BoardForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault('label_suffix', '')
#         super(BoardForm, self).__init__(*args, **kwargs)
#
#     class Meta:
#         model = Board
#         fields = ['title', 'content']