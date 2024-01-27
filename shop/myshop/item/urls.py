from django.urls import path 

from . import views 

app_name = 'item'


urlpatterns = [
      path('', views.items, name='items'),
      path('new/', views.new, name='new'),
     path('<int:pk>/', views.details, name='details'),
     path('<int:pk>/', views.delete, name='delete'),
     path('<int:pk>/', views.edit,name='edit')
    
]
