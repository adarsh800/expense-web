from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/auth/sign-in')
def tools(request):
    return render(request, 'tools/tools.html')