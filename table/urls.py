from django.urls import path
from . import views

app_name='table'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<tpk>', views.detail, name='detail'),
    path('delete/<tpk>', views.delete, name='delete'),
]
