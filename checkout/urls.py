from django.urls import path
from . import views

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('checkoutPayment/<int:message_to_checkout>', views.checkoutPayment, name='checkoutPayment'),
]
