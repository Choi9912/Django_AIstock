from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home' ),
    path('board/', board, name='board'),
    path('board/edit/<int:pk>', boardEdit, name='edit'),
    path('board/delete/<int:pk>', boardDelete, name='delete'),
]