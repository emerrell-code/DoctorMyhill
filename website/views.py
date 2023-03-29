from django.shortcuts import render

app_name = "website"
# Create your views here.
def index(request):
    return render(request, "website/index.html")

def mypractice(request):
    return render(request,"website/mypractice.html")

def myteam(request):
    return render(request,"website/myteam.html")

def find_us(request):
    return render(request,"website/find_us.html")