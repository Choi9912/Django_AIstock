from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("board/", views.board, name="board"),
    path("board/edit/<int:pk>/", views.board_edit, name="board_edit"),
    path("board/delete/<int:pk>/", views.board_delete, name="board_delete"),
]
