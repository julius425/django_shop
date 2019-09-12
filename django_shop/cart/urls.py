from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('order/', views.oder_summary, name='order'),
    path('create_order/<int:pk>', views.create_order, name='create_order'),
    path('complete/', views.complete, name='complete'),
    path('add/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>', views.remove_from_cart, name='remove_from_cart'),
]