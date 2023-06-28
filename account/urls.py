from django.urls import path
from account.views import UserRegistrationView,UserLoginView,UserProfileView,PasswordChangeView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('profile/', UserProfileView.as_view(),name='profile'),
    path('password_change/', PasswordChangeView.as_view(),name='pas_change'),
]
app_name = 'account'