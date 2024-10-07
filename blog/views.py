from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board
from .forms import BoardForm


def home(request):
    return render(request, "home.html")


def board(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect("board")
    else:
        form = BoardForm()

    boards = Board.objects.all()
    context = {
        "boardForm": form,
        "board": boards,  # 기존 게시글 목록
    }
    return render(request, "board.html", context)


@login_required
def board_edit(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect("board")
    else:
        form = BoardForm(instance=board)
    return render(request, "board_edit.html", {"form": form})


@login_required
def board_delete(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.delete()
    return redirect("board")
