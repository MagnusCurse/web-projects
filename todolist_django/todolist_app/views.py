from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "home.html")

def todo_list(request):
    items = TodoItem.objects.all()
    return render(request, "todos_list.html", {"todos": items})