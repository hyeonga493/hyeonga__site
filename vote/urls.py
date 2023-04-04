from django.urls import path
from . import views

app_name="vote"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('detail/<tpk>', views.detail, name='detail'),
    path('vote/<tpk>', views.vote, name='vote'),
    path('create/', views.create, name='create'),
    path('cancle/<tpk>', views.cancle, name='cancle'),
    path('delete/<tpk>', views.delete, name='delete'),
]
