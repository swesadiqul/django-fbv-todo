from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='home'),
    path('signup-user/', views.userRegister, name='signup'),
    path('user-login/', views.userLogin, name='user_login'),
    path('user-logout/', views.userLogout, name='user_logout'),
    path('change-password/', views.userChangePassword, name='change_password'),
    path('user-profile/', views.userProfile, name='user_profile'),

    #todo
    path('todo-list/', views.list_todo, name='todo-list'),
    path('todo-create/', views.create_todo, name='todo-create'),
    path('todo-update/<int:pk>/', views.update_todo, name='todo-update'),
    path('todo-delete/<int:pk>/', views.delete_todo, name='todo-delete'),
    path('search/', views.search, name='search'),
]

