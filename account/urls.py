from django.urls import path
from account.views import UserRegistrationView,UserLoginView,UserProfileView,PasswordChangeView,SendPasswordRestEmailView,PasswordResetView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('profile/', UserProfileView.as_view(),name='profile'),
    path('password_change/', PasswordChangeView.as_view(),name='pas_change'),
    path('password_reset/', SendPasswordRestEmailView.as_view(),name='pas_sendmail'),
    path('reset_confirm/<uid>/<token>/', PasswordResetView.as_view(),name='pas_reset'),
]
app_name = 'account'