from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('category-list/', views.category_list, name='category-list'),
    path('category-create/', views.category_create, name='create-category'),
    path('category-update/<str:pk>/', views.category_update, name='category-update'),
    path('category-delete/<str:pk>/', views.category_delete, name="delete-category"),

]