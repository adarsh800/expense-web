
from django.shortcuts import render, redirect
import datetime
import os
import json
from django.conf import settings
from .models import UserPreference,new_order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse




@login_required(login_url='/auth/sign-in')
def search_order(request):
    if request.method == 'POST':
        search_order_str = json.loads(request.body).get('searchText')


       
        data = new_order.objects.filter(first_name_new_order__istartswith = search_order_str, username=request.user) | new_order.objects.filter(
            second_name_new_order__istartswith = search_order_str, username=request.user) | new_order.objects.filter(
                email_new_order__istartswith = search_order_str, username=request.user) | new_order.objects.filter(
                    phone_number_new_order__istartswith = search_order_str, username=request.user) | new_order.objects.filter(
                        address_new_order__istartswith = search_order_str, username=request.user) | new_order.objects.filter(
                            address2_new_order__istartswith = search_order_str, username=request.user) | new_order.objects.filter(
                                city_new_order__istartswith = search_order_str, username=request.user) | new_order.objects.filter(
                                    pincode_new_order__istartswith = search_order_str, username=request.user) | new_order.objects.filter(
                                        state_new_order__istartswith = search_order_str, username=request.user)  
        order_data = data.values()
        return JsonResponse(list(order_data),safe=False)


@login_required(login_url='/auth/sign-in')
def order(request):

    currency_data = []
    order_data=[]
    
    user_preference = None


    
    order_data=new_order.objects.filter(username=request.user).all()
    paginator = Paginator(order_data,5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator,page_number)
    
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for k, v in data.items():
            currency_data.append({'name': k, 'value': v})

    exists = UserPreference.objects.filter(user=request.user).exists()

    if exists:
        user_preference = UserPreference.objects.get(user=request.user)
        
        
        # import pdb
        # pdb.set_trace()
    if request.method == 'GET':

        return render(request, 'orders/order.html', {'currencies': currency_data,
            'user_preference': user_preference,'order_context':order_data, 'page_obj':page_obj})
    else:

        currency = request.POST['currency']
        if exists:
            user_preference.currency = currency
            user_preference.save()
        else:
            UserPreference.objects.create(user=request.user, currency=currency)
        
        messages.success(request, 'Currency changes saved')
        return render(request, 'orders/order.html', {'currencies': currency_data, 
        'user_preference': user_preference,'order_context':order_data})
        


@login_required(login_url='/auth/sign-in')

def create_order(request):
    currency_data=[]
    

    if request.method == 'POST':
        first_name_new_order = request.POST['first_name']
        last_name_new_order = request.POST['last_name']
        email_new_order = request.POST['email_new_order']
        phone_number_new_order = request.POST['phone_number_new_order']
        address_new_order = request.POST['address_new_order']
        address2_new_order = request.POST['address2_new_order']
        city_new_order = request.POST['city_new_order']
        pincode_new_order = request.POST['pincode_new_order']
        state_new_order = request.POST['state_new_order']
        exists = UserPreference.objects.filter(user=request.user).exists()
        


        if exists:
           
            new_order.objects.create(user=request.user,username=request.user, date_new_order= datetime.datetime.now(), 
            first_name_new_order = first_name_new_order, second_name_new_order = last_name_new_order, 
            email_new_order = email_new_order, phone_number_new_order = phone_number_new_order, 
            address_new_order = address_new_order, address2_new_order = address2_new_order,
            city_new_order = city_new_order,pincode_new_order = pincode_new_order,state_new_order = state_new_order)
            
            
            
            # import pdb
            # pdb.set_trace()

            messages.success(request,'Order Created Successfully')
            return redirect('order')
            
            

            
        
        return render(request, 'orders/create-order.html')


    return render(request, 'orders/create-order.html')


def edit_order(request, id):
    order_data = new_order.objects.get(pk=id)
    # import pdb
    # pdb.set_trace()
    if request.method == 'GET':
        
        return render(request, 'orders/edit-order.html',{'order_data': order_data})
    

    if request.method == 'POST':
    
        first_name_new_order = request.POST['first_name']
        last_name_new_order = request.POST['last_name']
        email_new_order = request.POST['email_new_order']
        phone_number_new_order = request.POST['phone_number_new_order']
        address_new_order = request.POST['address_new_order']
        address2_new_order = request.POST['address2_new_order']
        city_new_order = request.POST['city_new_order']
        pincode_new_order = request.POST['pincode_new_order']
        state_new_order = request.POST['state_new_order']
        exists = UserPreference.objects.filter(user=request.user).exists()
        # import pdb
        # pdb.set_trace()
        if not first_name_new_order:
            messages.error(request, 'First name is required')
            return render(request, 'orders/edit-order.html', {'order_data': order_data})
        
        if not last_name_new_order:
            messages.error(request, 'Last Name is required')
            return render(request, 'orders/edit-order.html', {'order_data': order_data})

        order_data.first_name_new_order = first_name_new_order
        order_data.second_name_new_order = last_name_new_order
        order_data.email_new_order = email_new_order
        order_data.phone_number_new_order = phone_number_new_order
        order_data.address_new_order = address_new_order
        order_data.address2_new_order = address2_new_order
        order_data.city_new_order = city_new_order
        order_data.pincode_new_order = pincode_new_order
        order_data.state_new_order = state_new_order

        order_data.save()
        messages.success(request, 'Order updated  successfully')

        return redirect('order')

def delete_order(request,id):
    order_data = new_order.objects.get(pk=id)
    order_data.delete()
    messages.success(request, 'Order removed')
    return redirect('order')

    
    
        
   