from django.urls import path
from . import views

urlpatterns =  [
    path('', views.index_view),
    path('save/', views.saveMessage_view)
]