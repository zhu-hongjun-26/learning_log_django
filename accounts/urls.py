"""Defines URL patterns for accounts."""
from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    # 注册
    path('register/', views.register, name='register'),

    # 登录
    path('login/', auth_views.LoginView.as_view(), name='login'),

    # 登出
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # 修改密码
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            success_url=reverse_lazy('accounts:password_change_done')
        ),
        name='password_change',
    ),

    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done',
    ),
]
