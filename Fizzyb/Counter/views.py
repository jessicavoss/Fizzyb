from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "Counter/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'content': "Hello User!     " 
            + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def CurrentCount(request):
    return render(
        request,
        "Counter/CurrentCount.html",
        {
            'title' : "CurrentCount",
            'content' : "Example app page for Django."
        }
    )