from django.urls import path
from . import views

app_name = 'deposits'
urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products),
    path('deposit-products/', views.deposit_products),
]