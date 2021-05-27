from django.urls import path
from .views import index, login, home, logout_user


urlpatterns = [
    path('home/', home, name = 'home'),
    path('registration/', index, name = 'registration'),
    path('logout_user/', logout_user, name = 'logout_user'),
    path('login/', login, name = 'login'),
]
