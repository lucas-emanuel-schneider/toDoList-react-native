from django.urls import path
from . import views

urlpatterns = [
    path('get-csrf-token/', views.get_csrf_token, name='get-csrf-token'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('create-user/', views.createUser, name='create-user'),
    path('tasks/', views.taskList, name='tasks'),
    path('tasks/<str:pk>/', views.taskDetail, name='task'),
    path('create-task/', views.taskCreate, name='create-task'),
    path('update-task/<str:pk>/', views.taskUpdate, name='update-task'),
]
