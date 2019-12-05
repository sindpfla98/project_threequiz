from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import EmailField
from .validators import RegisteredEmailValidator
from django.core.files.images import get_image_dimensions
# 회원가입
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            # 8.19 소이 - 변경
            'email', 'name', 'birth', 'postcode', 'address', 'detail_address', 'ref_address', 'phone',
        ]

# 로그인
class LoginForm(AuthenticationForm):
    username = EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))

# 재발송 이메일
class VerificationEmailForm(forms.Form):
    email = EmailField(widget=forms.EmailInput(attrs={'autofocus': True}), validators=(EmailField.default_validators + [RegisteredEmailValidator()]))

# 190705 예림
# 마이페이지
class profileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['name', 'postcode', 'photo', 'address', 'detail_address', 'ref_address', 'phone' ]