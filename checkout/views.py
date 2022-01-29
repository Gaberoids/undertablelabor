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
    
    # creating intent. it looks like a huge dictionary
    intent = stripe.PaymentIntent.create(
        amount=stripe_total_payment,
        currency=settings.STRIPE_CURRENCY,
    )
    #  intent is a huge dictionary with a bunch of keys and values that comes from stripe. Client secret used below is one of the keys=value
    # intent type = <class 'stripe.api_resources.payment_intent.PaymentIntent'>

    if request.method == 'POST':
        # use below line when you want to get form inputs from a .html form
        form = MessageToServiceForm(request.POST)
        if form.is_valid():
            print("form inside form is valid ---------***********-----------------**************------------")
            print(form)
            created_message = form.save()
            created_message_id = created_message.id
            # above integer id
            created_message_checkout = ContactMessage.objects.get(pk=created_message_id)
            # created_message_checkout = ContactMessage object (90)
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
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)
