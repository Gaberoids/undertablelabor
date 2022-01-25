from django.shortcuts import render
from contact_services.models import ContactMessage
from contact_services.forms import MessageToServiceForm
from django.contrib import messages


# Create your views here.
def checkout(request):
    # messages below place holderstween logged in user and service rpovider

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
    
    all_messages = ContactMessage.objects.all()
    # print(" for loop all messages to get the table value ---------***********-----------------**************------------")
    # for x in all_messages:
    #     print(x.m_title, x.m_body, x.m_sender, x.m_receiver)
    template = 'checkout/checkout.html'
    context = {
        'message_to_checkout': created_message_checkout,
        # 'on_profile_page': True
        'stripe_public_key': 'pk_test_51JoyKmIC9OHyTnCzT2FCFBpAtTY3Rzd8N6zgOKEBEF2sU9c4I8zdoeBB8u2eGmvb0I8B5gQ5SbLgtVlQ5KUcHgLo0064z7vemP',
        'stripe_client_key': 'client key test',
    }
    return render(request, template, context)
