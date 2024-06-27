from django.urls import path
from .views import login, register, home, groups, account

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('groups/', groups, name='groups'),
    path('account/', account, name='account')
]