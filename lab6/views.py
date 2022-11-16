from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from django.db import connection
from .models import Feedback
import js2py

# Create your views here.
def index(request):
    if request.method == 'POST':
        del request.session['username']
        return render(request, 'index.html', {"username" : ""})
    else:
        if request.session.has_key('username'):
            username = request.session['username']
            return render(request,  'index.html', {"username" : username})
        else:
            return render(request, 'index.html', {"username" : ""})

def feedback(request):
    args = {}
    if request.method == 'POST':
        try:
            fileboolean = request.FILES['nationalID']
        except:
            fileboolean = False
        if request.POST.get("message") is not None and fileboolean == True:
            Feedback.objects.create(message=request.POST.get("message"), nationalID=request.FILES['nationalID'])
            return render(request, 'index.html')
        else:
            return render(request, 'feedback.html')
    else:
        return render(request, 'feedback.html')

def search(request):
    if request.method == 'POST':
        if request.POST.get("usersearch") is not None:
            cursor = connection.cursor()
            query = "SELECT city, street FROM lab6_branch WHERE country = '" + str(request.POST.get("usersearch")) +"'"
            branches = cursor.execute(query)
            return render(request, 'search.html', {"branches" : branches , "searched": request.POST.get("usersearch")})
    return render(request, 'search.html', {"searched": ""})