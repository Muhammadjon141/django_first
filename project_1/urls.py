from django.urls import path
from .views import login, register, home, groups, account, index, endex, Web_sahifa

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('groups/', groups, name='groups'),
    path('account/', account, name='account'),
    path('index/', index, name='index'),
    path('endex/', endex, name='endex'),
    path('Web_sahifa/', Web_sahifa, name="Web_sahifa")
]