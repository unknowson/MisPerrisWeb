from django.contrib import admin
from django.urls import path, include
#from django.contrib.auth.views import LoginView
#Aca estoy cambiando la importacion de la vista por el de abajo :p
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [ 
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),
    path('', views.Mostrar, name='Trabajo_Perrits_good'),
    path('rescatados', login_required(views.listarRescatados), name='rescatados'),
    path('reset', auth_views.PasswordResetView.as_view(), name='reset'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_confirm/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]