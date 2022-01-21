from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/auth/sign-in')
def index(request):
    return render(request, 'e_base.html')

@login_required(login_url='/auth/sign-in')
def dashboard(request):
    return render(request, 'expensedashboard/index_dashboard.html')

@login_required(login_url='/auth/sign-in')
def billing(request):
    return render(request, 'expensedashboard/billing.html')

@login_required(login_url='/auth/sign-in')
def subexpense(request):
    return render(request, 'expensedashboard/table.html')

@login_required(login_url='/auth/sign-in')
def notifications(request):
    return render(request, 'expensedashboard/notifications.html')

@login_required(login_url='/auth/sign-in')
def profile(request):
    return render(request, 'expensedashboard/profile.html')
