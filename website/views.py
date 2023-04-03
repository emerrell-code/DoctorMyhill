import markdown
from django.shortcuts import render

from . import util

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

def contact_us(request):
    return render(request,"website/contact_us.html")

def address(request):
    return render(request,"website/addressing_the_causes_and_squashing_the Symptoms.html")

def list(request):
    return render(request, "website/list.html", {
        "entries": util.list_entries()
    })

def ecological(request):
    return render(request,"website/ecological.html")

def books(request):
    return render(request, "website/books.html")

def markdown_2_html(title):
    page = util.get_entry(title)
    markdowner = markdown.Markdown()
    # if the page doesn't exit return none
    if page == None:
        return None
    # if the page does exist then convert the page into html
    else:
        return markdowner.convert(page)
    


def entry(request, title):
    HtmlContent = markdown_2_html(title)
        # if the page doesn't exist then show an error message
    if HtmlContent == None:
        return render(request, "website/error.html", {
            "message": "This page does not exist"
        })
        # if the page exists then show the page with the same title
    else:
        s_title = title.replace("_", " ")
        return render(request, "website/entry.html", {
            "title": s_title,
            "page": HtmlContent
        })