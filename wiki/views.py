from django.shortcuts import render

app_name = "wiki"
# Create your views here.
def wiki(request):
    return render(request, "wiki/wiki.html")