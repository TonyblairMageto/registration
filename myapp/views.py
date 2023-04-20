from django.shortcuts import render,redirect
from .models import Member


# Create your views here.
def register(request):
    if request.method=='post':
        member=Member(firstname=request.post['firstname'],lastname=request.post['lastname'],password=request.post['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html',)

def login(request):
    return render(request, 'login.html')

def home(request):
    if request.method == 'post':
       if Member.objects.filter(username=request.post['username'], password=request.post['password']).exists():
           member = Member.objects.get(username=request.post['username'], password=request.post['password'])
           return render(request, 'home.html', {'member': member})
       else:
             return render(request, 'login.html')


