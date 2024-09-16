
from django.urls import path
from django.contrib.auth import views as auth_views
from user_app.views import register,login_page,logout_view,profile,profileupdate


urlpatterns = [
    path('register/',register,name='register'),
    path('login_page/',login_page,name='login_page'),
    path('logout/',logout_view,name='logout_view'),
    path('profile/',profile,name='profile'),
    path('profile/update/',profileupdate,name='profileupdate-page'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='user_app/passwordchange.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='user_app/passwordchanage_done.html'), name='password_change_done'),
]
