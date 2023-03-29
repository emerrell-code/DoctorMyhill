from django.shortcuts import render

app_name = "books" 
# Create your views here.
def books(request):
    return render(request, "books/books.html")