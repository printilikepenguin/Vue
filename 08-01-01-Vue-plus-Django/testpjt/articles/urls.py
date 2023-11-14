from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('review/', views.review),
    path('board/', views.board),
    path('faq/', views.faq),
]
