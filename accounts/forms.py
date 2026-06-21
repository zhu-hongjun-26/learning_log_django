from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 中文 label
        self.fields['username'].label = '用户名'
        self.fields['password1'].label = '密码'
        self.fields['password2'].label = '确认密码'

        # 中文 help_text
        self.fields['username'].help_text = '请输入 150 个字符以内的字母、数字或 @ . + - _'
        self.fields['password1'].help_text = '至少 8 位，不能是常见密码'
        self.fields['password2'].help_text = '再次输入相同的密码'

        # 中文错误提示（可选）
        self.fields['password2'].error_messages.update({
            'password_mismatch': '两次输入的密码不一致'
        })
        