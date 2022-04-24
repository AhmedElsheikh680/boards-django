from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import Board,Post
from django.shortcuts import render,get_object_or_404,redirect
from .forms import NewTopicForm
# Create your views here.

def home(request):
    boards = Board.objects.all()
    context = {
        "boards": boards
    }
    return render(request, 'home.html', context)


def board_topics(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'topics.html', {"board": board})

def new_topic(request, board_id):
    board = get_object_or_404(Board, pk = board_id)

    user = User.objects.first()
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = user
            topic.save()
            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                created_by = user,
                topic = topic
            )
            return redirect('board_topics', board_id=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {"board": board, "form": form})



