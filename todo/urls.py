from django.urls import path
from . import views
from accounts.views import login_view, register_view, logout_view

urlpatterns = [
    path('', views.index, name = 'index'),
    path('delete/<list_id>', views.delete, name="delete"),
    path('check/<list_id>', views.check, name="check"),
    path('uncheck/<list_id>', views.uncheck, name="uncheck"),
    path('edit/<list_id>', views.edit, name="edit"),
    path('accounts/login/', login_view, name="login"),
    path('accounts/register/', register_view, name="register"),
    path('accounts/logout/', logout_view, name="logout"),
]