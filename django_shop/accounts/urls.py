from django.urls import path, include
from . import views


app_name = 'accounts'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('edit/<int:pk>', views.profile_edit, name='edit'),
    path('signup/', views.sign_up, name='signup'),
    path('', include('django.contrib.auth.urls'))
]
