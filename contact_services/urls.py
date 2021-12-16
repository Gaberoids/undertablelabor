from django.urls import path
from . import views

urlpatterns = [
    path('contact_service/<username>', views.contact_service, name='contact_service'),
    path('delete_service_message/<int:message_id>/<username>/', views.delete_service_message, name='delete_service_message'),

    # path('order_history/<order_number>', views.order_history, name='order_history'),
]
