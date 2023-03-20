from django.shortcuts import render

app_name = "website"
# Create your views here.
def index(request):
    return render(request, "website/index.html")