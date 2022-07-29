from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('', index, name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout',),
]
