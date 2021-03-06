from user_info.views import (
    sign_up,
    signin,
    profile_create,
    profile_detail,
    profile_edit,
)
from django.urls import path
from django.contrib.auth import views as LoginView
from django.contrib.auth import views as LogoutView

urlpatterns = [
    path('signup/', sign_up, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', LogoutView.logout, name='logout'),
    # path('profile/', profile_check, name='profile'),
    path('profile-create/', profile_create, name='profile-create'),
    path('profile-detail/<int:id>/', profile_detail, name='profile-detail'),
    path('profile-detail/', profile_detail, name='profile'),
    path('profile-edit/', profile_edit, name='profile-edit'),
]
