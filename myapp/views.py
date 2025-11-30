from django.shortcuts import render, redirect
from.models import*
import random
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')  
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None: 
            login(request,user) 
            return redirect('/dashboard')   
        else:
            messages.error(request, "Invalid username or password") 
            return redirect('/login') 
               
    
    return render(request, 'user_login.html')


def user_signup(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        phone = request.POST.get('phone')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        photo=request.FILES.get('photo')

        while True:
            random_number=random.randint(1000,9999)
            if not UserDetails.objects.filter(accno=random_number).exists():
                accno=random_number
                break 


        print(username,email,password,confirm_password,phone)
        if not UserDetails.objects.filter(username=username).exists():
            if password == confirm_password:
                UserDetails.objects.create_user(
                    
                username=username,
                email=email, 
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                photo=photo,
                accno=accno 
                )
                messages.success(request,'New User Created Successfully')
                return redirect('/login')

            else:
                messages.warning(request,'your password and retype password are not match')
                return redirect('/user_signup')
         
        else:
            messages.success(request,'The User was already exist')
            return render(request,'user_signup.html')   
    return render(request, 'user_signup.html') 


@login_required(login_url='/login')
def dashboard(request):
    data=transaction_model.objects.filter(customer_id=request.user.id)
    return render(request,'dashboard.html',{'data':data})

@login_required(login_url='/login')
def deposite(request):
    if request.method=='POST':
        deposit_amt=int(request.POST.get('deposite_amount'))
        old_bal=UserDetails.objects.get(id=request.user.id).balance
        new_bal=old_bal+deposit_amt
        UserDetails.objects.filter(id=request.user.id).update(balance=new_bal)
        
        transaction_model.objects.create(customer_id=request.user.id,transaction_type='Deposite',amount=deposit_amt,balance=new_bal)
        messages.success(request,'Amount Deposited Successfully')
        return redirect('/dashboard')
    return render(request,'deposite.html')

@login_required(login_url='/login')
def withdrawn(request):
    if request.method=='POST':
        withdrawn_amt=int(request.POST.get('Withdrawn_amount'))
        old_bal=UserDetails.objects.get(id=request.user.id).balance
        if old_bal>=withdrawn_amt:
            new_bal=old_bal-withdrawn_amt
            UserDetails.objects.filter(id=request.user.id).update(balance=new_bal)
        
            transaction_model.objects.create(customer_id=request.user.id,transaction_type='Withdrawn',amount=withdrawn_amt,balance=new_bal)
            messages.success(request,'Amount Withdrawn Successfully')
            return redirect('/dashboard')
        else:
            messages.error(request,'Insufficient Balance')  
            redirect('/withdrawn') 
    return render(request,'withdrawn.html')


@login_required(login_url='/login')
def balance(request):
     balance = UserDetails.objects.get(id=request.user.id).balance
     return render(request,'balance.html',{'balance':balance})    


def user_logout(request):
    logout(request)
    return redirect('/index')