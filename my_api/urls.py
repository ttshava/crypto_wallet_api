from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('btc-address-list/', views.btcList, name="btc-address-list"),
    path('btc-detail/<str:pk>/', views.btcDetail, name="btc-Detail"),
    path('btc-create/', views.btcCreate, name="btc-Create"),

    path('eth-address-list/', views.ethList, name="eth-address-list"),
    path('eth-detail/<str:pk>/', views.ethDetail, name="eth-Detail"),
    path('eth-create/', views.ethCreate, name="eth-Create"),

]