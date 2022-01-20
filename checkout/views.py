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
            # created_message_checkout = ContactMessage.objects.get(pk=created_message_id)
            messages.success(request, 'Message created successfully')
        else:
            messages.error(request,
                           ('Message failed. Please ensure '
                            'the form is valid.'))    
    
    all_messages = ContactMessage.objects.all()
    print(" for loop all messages to get the table value ---------***********-----------------**************------------")
    for x in all_messages:
        print(x.m_title, x.m_body, x.m_sender, x.m_receiver)
    template = 'checkout/checkout.html'
    context = {
        'all_messages': all_messages,
        # 'on_profile_page': True
    }
    return render(request, template, context)
