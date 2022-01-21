from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/auth/sign-in')
def support(request):
    return render(request, 'support/support.html')