from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_profile, name='my_profile'),
    path('all_services', views.all_services, name='all_services'),
    path('delete_service_message/<int:message_id>/<username>/', views.delete_service_message, name='delete_service_message'),

    # path('order_history/<order_number>', views.order_history, name='order_history'),
]
