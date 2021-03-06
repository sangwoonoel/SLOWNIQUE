from django import forms
from .models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField, AuthenticationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, label = '아이디', widget=forms.TextInput(attrs={'placeholder': '아이디를 입력해주세요'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력해주세요'}), label = '비밀번호')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                raise forms.ValidationError('password is wrong!!!')
        except User.DoesNotExist:
            raise forms.ValidationError('No User!!!')

# class SignUpForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput, label='비밀번호')
#     password2 = forms.CharField(widget=forms.PasswordInput, label = '비밀번호확인')

#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email', 'nickname']

#         labels = {
#                 'username': '아이디',
#                 'email': '이메일',
#                 'nickname': '닉네임',
#             }

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '아이디'}),
    error_messages={
                'unique': '이미 존재하는 아이디입니다.'
            })
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '비밀번호'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '비밀번호 확인'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': '이메일'}))
    nickname = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': '닉네임'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'nickname')

class AuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            '올바른 아이디와 비밀번호를 입력해 주세요.'
        ),
        'inactive': _('비활성화된 계정입니다.'),
    }
class CustomLoginView(LoginView):
    authentication_form = AuthForm

class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label='Password', widget=forms.HiddenInput())
    class Meta:
        model = get_user_model()
        fields = ['nickname', 'email', 'image']



