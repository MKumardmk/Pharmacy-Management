from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category
from .forms import CategoryForm

def index(request):
    title = "categories"
    categories = Category.objects.all()
    return render(request, 'categories.html', {'title': title, 'categories': categories})

def store(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category has been added')
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})

def update(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category has been updated')
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'edit_category.html', {'form': form, 'category': category})

def destroy(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    messages.success(request, 'Category has been deleted')
    return redirect('categories')




# dashboard

# from django.shortcuts import render
# from django.db.models import Count, Sum
# from .models import Purchase, Category, Supplier, Sales
# from chartjs.views.lines import BaseLineChartView

# def DashboardView(request):
#     title = "dashboard"
    
#     total_purchases = Purchase.objects.filter(expiry_date__date=datetime.date.today()).count()
#     total_categories = Category.objects.count()
#     total_suppliers = Supplier.objects.count()
#     total_sales = Sales.objects.count()
    
#     pie_chart_data = {
#         'labels': ['Total Purchases', 'Total Suppliers', 'Total Sales'],
#         'datasets': [
#             {
#                 'backgroundColor': ['#FF6384', '#36A2EB', '#7bb13c'],
#                 'hoverBackgroundColor': ['#FF6384', '#36A2EB', '#7bb13c'],
#                 'data': [total_purchases, total_suppliers, total_sales]
#             }
#         ]
#     }
    
#     total_expired_products = Purchase.objects.filter(expiry_date__date=datetime.date.today()).count()
#     latest_sales = Sales.objects.filter(created_at__date=datetime.date.today())
#     today_sales = Sales.objects.filter(created_at__date=datetime.date.today()).aggregate(Sum('total_price'))['total_price__sum']
    
#     context = {
#         'title': title,
#         'pie_chart_data': pie_chart_data,
#         'total_expired_products': total_expired_products,
#         'latest_sales': latest_sales,
#         'today_sales': today_sales,
#         'total_categories': total_categories
#     }
    
#     return render(request, 'dashboard.html', context)










# ========================================
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Product, Purchase
from datetime import date

class ProductView(View):
    def get(self, request):
        title = "products"
        products = Product.objects.select_related('purchase').all()
    
        return render(request, 'products.html', {'title': title, 'products': products})
    
    def post(self, request):
        product_name = request.POST.get('product')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        description = request.POST.get('description')
        
        if not (product_name and price):
            return HttpResponse("Invalid request")
        
        purchase = Purchase.objects.get(id=product_name)
        price = float(price)
        
        if discount and float(discount) > 0:
            price *= float(discount)
        
        Product.objects.create(purchase=purchase, price=price, discount=discount, description=description)
        
        return redirect('products')
