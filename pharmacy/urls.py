from django.urls import path
from . import views


urlpatterns = [
    path('',views.login_user,name='login'),
    path('dashboard',views.home,name='dashboard'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_user,name='logout'),
    path('categories',views.categories,name='categories'),
     path('forgot-password/',views.forgot_password,name='forgot_password'),
    path('password-reset/<uidb64>/<token>/', views.reset_password, name='reset_password'),




    # products
    path('products',views.products,name='products'),
    path('products/add',views.products,name='add_product'),
    path('expired-products',views.expired_products,name='expired_products'),
    path('outstock-products',views.outstock_products,name='outstock_products'),
#     Route::get('expired-products',[ProductController::class,'expired'])->name('expired');
#     Route::get('products/{product}',[ProductController::class,'show'])->name('edit-product');
#     Route::get('outstock-products',[ProductController::class,'outstock'])->name('outstock');
#     Route::post('products/create',[ProductController::class,'store']);
#     Route::post('products/{product}',[ProductController::class,'update']);
#     Route::delete('products',[ProductController::class,'destroy']);




    # purchase
    path('purchases',views.purchases,name='purchases'),
    path('add-purchase',views.add_purchase,name='add_purchase'),
    # Route::get('purchases',[PurchaseController::class,'index'])->name('purchases');
    #     Route::get('add-purchase',[PurchaseController::class,'create'])->name('add-purchase');
    #     Route::post('add-purchase',[PurchaseController::class,'store']);
    #     Route::get('purchases/{purchase}',[PurchaseController::class,'show'])->name('edit-purchase');
    #     Route::put('purchases/{purchase}',[PurchaseController::class,'update']);
    #     Route::delete('purchases',[PurchaseController::class,'destroy']);


    # sales
     path('sales',views.sales,name='sales'),
    # Route::get('sales',[SalesController::class,'index'])->name('sales');
#     Route::post('sales',[SalesController::class,'store']);
#     Route::put('sales',[SalesController::class,'update']);
#     Route::delete('sales',[SalesController::class,'destroy']);

    # suppliers
     path('suppliers',views.suppliers,name='suppliers'),
    #     Route::get('suppliers',[SupplierController::class,'index'])->name('suppliers');
#     Route::get('add-supplier',[SupplierController::class,'create'])->name('add-supplier');
#     Route::post('add-supplier',[SupplierController::class,'store']);
#     Route::get('suppliers/{supplier}',[SupplierController::class,'show'])->name('edit-supplier');
#     Route::delete('suppliers',[SupplierController::class,'destroy']);
#     Route::put('suppliers/{supplier}}',[SupplierController::class,'update'])->name('edit-supplier');

    #reports
    path('reports',views.reports,name='reports'),
    # Route::get('reports',[ReportController::class,'index'])->name('reports');
#     Route::post('reports',[ReportController::class,'getData']);


    # permissions
    path('permissions',views.permissions,name="permissions"),
    #     Route::get('permissions',[PermissionController::class,'index'])->name('permissions');
#     Route::post('permissions',[PermissionController::class,'store']);
#     Route::put('permissions',[PermissionController::class,'update']);
#     Route::delete('permissions',[PermissionController::class,'destroy']);

# profile
    path('profile',views.profile,name='profile'),
# Route::get('profile',[UserController::class,'profile'])->name('profile');
#     Route::post('profile',[UserController::class,'updateProfile']);
#     Route::put('profile',[UserController::class,'updatePassword'])->name('update-password');




    path('settings/', views.settings, name='settings'),



]



# Route::group(['middleware'=>['guest']],function (){
#     Route::get('login',[AuthController::class,'index'])->name('login');
#     Route::post('login',[AuthController::class,'login']);
#     Route::get('register',[AuthController::class,'register'])->name('register');
#     Route::post('register',[AuthController::class,'store']); 

   

#     Route::get('forgot-password',[AuthController::class,'forgotView'])->name('forgot-password');
#     Route::post('forgot-password',[AuthController::class,'reset']);
# });

# Route::group(['middleware'=>['auth']],function (){
#     Route::get('dashboard',[DashboardController::class,'index'])->name('dashboard');
#     Route::get('logout',[AuthController::class,'logout'])->name('logout');

#     Route::get('categories',[CategoryController::class,'index'])->name('categories');
#     Route::post('categories',[CategoryController::class,'store']);
#     Route::put('categories',[CategoryController::class,'update']);
#     Route::delete('categories',[CategoryController::class,'destroy']);

#     



#   

#     Route::get('sales',[SalesController::class,'index'])->name('sales');
#     Route::post('sales',[SalesController::class,'store']);
#     Route::put('sales',[SalesController::class,'update']);
#     Route::delete('sales',[SalesController::class,'destroy']);



#     Route::get('roles',[RoleController::class,'index'])->name('roles');
#     Route::post('roles',[RoleController::class,'store']);
#     Route::put('roles',[RoleController::class,'update']);
#     Route::delete('roles',[RoleController::class,'destroy']);

#     Route::get('users',[UserController::class,'index'])->name('users');
#     Route::post('users',[UserController::class,'store']);
#     Route::put('users',[UserController::class,'update']);
#     Route::delete('users',[UserController::class,'destroy']);

#     Route::get('profile',[UserController::class,'profile'])->name('profile');
#     Route::post('profile',[UserController::class,'updateProfile']);
#     Route::put('profile',[UserController::class,'updatePassword'])->name('update-password');

#     Route::get('settings',[SettingController::class,'index'])->name('settings');

#     Route::get('notification',[NotificationController::class,'markAsRead'])->name('mark-as-read');
#     Route::get('notification-read',[NotificationController::class,'read'])->name('read');

#     Route::get('reports',[ReportController::class,'index'])->name('reports');
#     Route::post('reports',[ReportController::class,'getData']);

#     Route::get('backup',[BackupController::class,'index'])->name('backup-app');
#     Route::get('backup-app',[BackupController::class,'database'])->name('backup-db');
# });

# Route::get('/', function () {
#     return redirect()->route('dashboard');
# });
