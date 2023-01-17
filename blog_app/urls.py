from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('', index, name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout',),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('search/', SearchPost.as_view(), name='search_results'),
    path('feedback/', ContactFormView.as_view(), name='contact_us'),
    path('tag/<slug:slug>/', TagView.as_view(), name="tag"),
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile'),
]
