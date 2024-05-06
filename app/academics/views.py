from django.shortcuts import redirect, render
from django.http import HttpResponse 
from .forms import UserForm
# Create your views here.
def index (request):
    return index("Hello world, Yo're at the academics index")

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            form = UserForm()
        return render (request, 'academics/create_user.html',{'form':form})