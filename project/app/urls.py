from django.urls import path
from . import views


app_name = 'app'



urlpatterns =   [
  path('', views.book, name='book'),
    path('creat/', views.create, name='create'),
    path('creat/update/<int:id>', views.update, name='update'),
    path('creat/update/delete/<int:id>', views.delete, name='delete'),
] 
    