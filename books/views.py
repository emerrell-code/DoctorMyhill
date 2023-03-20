from django.shortcuts import render

app_name = "books" 
# Create your views here.
def index(request):
    return render(request, "books/index.html")