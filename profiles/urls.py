from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_profile, name='my_profile'),
    path('all_services', views.all_services, name='all_services'),
    # path('order_history/<order_number>', views.order_history, name='order_history'),
]
