from django.shortcuts import render
from contact_services.models import ContactMessage
from contact_services.forms import MessageToServiceForm
from django.contrib import messages

# two next lines are for stripe
from django.conf import settings
import stripe


# Create your views here.
def checkout(request):
    # messages below place holderstween logged in user and service rpovider
 
    # stripe
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_total_payment = 100
    # in stripe, 100 = $1.00
    stripe.api_key = stripe_secret_key
    print("stripe_api_key = ---------***********-----------------**************------------")   
    print(stripe.api_key)
    print(stripe_public_key)
    print(stripe_secret_key)
    intent = stripe.PaymentIntent.create(
        amount=stripe_total_payment,
        currency=settings.STRIPE_CURRENCY,
    )
    print("intent ---------***********-----------------**************------------")
    print(intent)

    if request.method == 'POST':
        form = MessageToServiceForm(request.POST)
        if form.is_valid():
            created_message = form.save()
            # 
            created_message_id = created_message.id
            # above integer id
            created_message_checkout = ContactMessage.objects.get(pk=created_message_id)
            print("created_message_checkout ---------***********-----------------**************------------")
            print(created_message_checkout)
            messages.success(request, 'Message created successfully')
        else:
            messages.error(request,
                           ('Message failed. Please ensure '
                            'the form is valid.'))    
    
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')
    
    all_messages = ContactMessage.objects.all()
    # print(" for loop all messages to get the table value ---------***********-----------------**************------------")
    # for x in all_messages:
    #     print(x.m_title, x.m_body, x.m_sender, x.m_receiver)
    template = 'checkout/checkout.html'
    context = {
        'message_to_checkout': created_message_checkout,
        # 'on_profile_page': True
        'stripe_public_key': stripe_public_key,
        'stripe_client_key': intent.client_secret,
    }
    return render(request, template, context)
