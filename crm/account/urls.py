from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user/<str:pk>/', views.userPage, name="user-page"),
    path('products/', views.product, name="products"),
    # path('customer/<str:pk>/', views.customer, name="customer"), #dynamic routing

    path('customer_list/', views.customer_list_view, name="customer_list"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('update_customer/<str:pk>/', views.updateCustomer, name='update_customer'),
    path('delete_customer/<str:pk>/', views.deleteCustomer, name='delete_customer'),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),

    path('create_product/', views.createProduct, name="create_product"),
]