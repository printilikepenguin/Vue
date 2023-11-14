from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('signup/', views.signup),
]
