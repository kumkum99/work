from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # In urls.py
    path('login/index/', views.index_view, name='index1'),
    path('about/', views.about_view, name='about'),
    path('news/', views.news_view, name='news'),
    path('contact/', views.contact_view, name='contact'),
    path('farming/', views.farming_views, name='farming'),
    path('newsd/', views.newsd_views, name='newsd'),
    path('shop/', views.shop_views, name='shop'),
    path('ourproduct/', views.ourproduct_views, name='ourproduct'),
    path('bestfarmers/', views.bestfarmers_views, name='bestfarmers'),
    path('weather/', views.weather_views, name='weather'),
    path('signup/', views.signup, name='signup'),
    path('signup/login', views.login, name='login'),
    path('saveenquiry/', views.saveEnquiry, name='saveenquiry'),
    path('farming/aprentice/', views.aprenticeship, name='aprenticeship'),
    path('cart/', views.cart_page, name='cart_page'),
    path('pay/', views.pay, name='pay'),

]
