from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.categories_list, name='categories'),
    path('<slug>/', views.product_list, name='products'),
    path('<category_slug>/<int:pk>/', views.product_detail, name='product'),
]