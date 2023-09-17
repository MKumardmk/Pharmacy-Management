from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Q


from . import forms


from .utils import send_html_email



from django.views import View
# from django.contrib.auth.hashers import check_password


from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth import get_user_model

# Create your views here.
def login_user(request):
    form=forms.LoginForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        user=authenticate(request=request,username=email,password=password)
        if user:
            login(request=request,user=user)
            return redirect('dashboard')
        else:
            pass
    title="login"
    return render(request,'auth/login.html',locals())

def register(request):
    form=forms.RegisterForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        name=form.cleaned_data.get('name')
        user=User.objects.create_user(username=email,email=email,first_name=name,password=password)
        login(request=request,user=user)
        return redirect('dashboard')
    print(form.errors)
    title="register"
    return render(request,'auth/register.html',locals())
def logout_user(request):
    logout(request=request)
    return redirect('login')


def forgot_password(request):
    form=forms.ForgotPasswordForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        email= form.cleaned_data.get('email')
        user = User.objects.filter(Q(username__iexact=email)| Q(email__iexact=email)).first()
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = default_token_generator.make_token(user)
        reset_link=f"{request.build_absolute_uri('/')}password-reset/{uid}/{token}/"
        message="Email send Successfully"
        data={}
        data['link']=reset_link
        email_msg= send_html_email(
            subject='Password Reset',
            to_list=['mohan@webchirpy.com',email],
            template='email/forgot_password.html',
            context={"link":reset_link}

        )
        redirect('login')
    return render(request,'auth/forgot-password.html',locals())


def reset_password(request,uidb64,token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = get_user_model().objects.get(pk=uid)
    if request.method =='POST' and default_token_generator.check_token(user, token):
        new_password = request.POST.get('password')
        user.set_password(new_password)
        user.save()
        return redirect('student_login')
    elif get_user_model().DoesNotExist:
        error_message='User not found'
    elif request.method =='POST':
        error_message='Invalid Token'
    return render(request=request,template_name='',context=locals())

def home(request):
    total_purchases="260"
    total_categorie="290"
    total_suppliers="250"
    total_sales="120"
    return render(request,'dashboard.html',locals())



def categories(request):
    title = "categories";
    categories =[]
    return render(request,'categories.html',locals())

def products(request):
   
    title = "products";
    products = []
    return render(request,'products.html',locals())

def create_product(request):
    title= "Add Product";
    products = []
    return render('add-product.html',locals())

def expired_products(request):
    title = "expired Products";
    products = []
        
    return render(request,'expired.html',locals())



def outstock_products(request):
        title = "outstocked Products";
        # products = Purchase::where('quantity', '<=', 0)->get();
        # product = Purchase::where('quantity', '<=', 0)->first();
        products=[]
        return render(request,'outstock.html',locals());





def purchases(request):
    
    title = "purchases";
    # purchases = Purchase::with('category')->get();
    purchases = []
    return render(request,'purchases.html',locals())
    
    
 
def add_purchase(request):
    
    title = "add Purhase";
    categories = []
    suppliers = []
    return render(request,'add-purchase.html',locals())




def sales(request):

    title = "sales";
    products = []
    sales = []
                
    return render(request,'sales.html',locals())



def suppliers(request):
    title ="Suppliers";
    suppliers = []
    return render(request,'suppliers.html',locals())



def reports(request):
    title = "generate Reports";
    return render(request,'reports.html',locals())


def permissions(request):
    title = "Permissions";
    permissions =[]
    return render(request,'permissions.html',locals())


def profile(request):
    title = "profile";
    roles = []
    return render(request,'profile.html',locals())


# from django.shortcuts import render
# from .models import Role, Permission

# def index(request):
#     title = "user Roles"
#     roles = Role.objects.prefetch_related('permissions').all()
#     permissions = Permission.objects.all()
#     return render(request, 'roles.html', {
#         'title': title,
#         'roles': roles,
#         'permissions': permissions
#     })



# from django.shortcuts import redirect
# from django.contrib import messages
# from django.core.management import call_command

# def index(request):
#     call_command('backup', '--disable-notifications')
#     messages.success(request, 'Backup has been made')
#     return redirect('dashboard')

# def database(request):
#     call_command('backup', '--only-db', '--disable-notifications')
#     messages.success(request, 'Database has been backed up')
#     return redirect('dashboard')

def settings(request):
    return render(request,'settings.html',locals())

