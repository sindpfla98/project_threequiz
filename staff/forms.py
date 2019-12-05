from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget

class BoardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(BoardForm, self).__init__(*args, **kwargs)

    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Board
        fields = ['title', 'content']
# 질문 폼
class QForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(QForm, self).__init__(*args, **kwargs)
    
    # 10.13 소이 - form 디자인 수정
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '제목을 입력해주세요.'}))  # 아래의 widget도 써줘야 작동
    question = forms.CharField(widget=SummernoteWidget())

    title.widget.attrs['placeholder'] = "제목을 입력해주세요."
    question.widget.attrs['class'] = "qform_content"
    
    class Meta:
        model = QnA
        fields = ['title', 'question', 'lock']

# 답변 폼
class AForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(AForm, self).__init__(*args, **kwargs)

    answer = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = QnA
        fields = ['answer']

