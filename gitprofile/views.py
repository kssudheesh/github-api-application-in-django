from django.shortcuts import render, HttpResponse
import requests
import json
import dateutil.parser

# Create your views here.

def index(request):
    content = {}
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/'+username)
        content = req.json()
        content['created_at'] = dateutil.parser.parse(content['created_at'])
    return render(request, 'gitprofile/index.html', content)
