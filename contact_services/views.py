from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from profiles.models import UserProfile
from .models import ContactMessage
from .forms import MessageToServiceForm
import gc
# import pprint as pp


def contact_service(request, username):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, default_aka=username)
    # profile=admin1 = user loggedin
    # type= class = <class 'profiles.models.UserProfile'>

    if request.method == 'POST':
        form = MessageToServiceForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Message created successfully')
        else:
            messages.error(request,
                           ('Message failed. Please ensure '
                            'the form is valid.'))
# what the heck the next two lines are doing???
    form = MessageToServiceForm()

    # prepopulate m_sender and m_receiver
    if request.user.is_authenticated:
        print("user authenticated---------***********-----------------**************------------")
        try:
            
            print("inside of try is auth---------***********-----------------**************------------")
            m_profile = UserProfile.objects.get(user=request.user)
            print(m_profile.user.email)
            print(m_profile.user)
            m_message_form = MessageToServiceForm(initial={
                'm_sender': m_profile.user,
                'm_sender_email': m_profile.user.email,
            })
            print("print form inside the try after form1---------***********-----------------**************------------")
            print(m_message_form)
        except UserProfile.DoesNotExist:
            print("inside of try except---------***********-----------------**************------------")
            order_form = OrderForm()
    else:
        print("user not authenticated---------***********-----------------**************------------")
        try:
            print("inside of try isnotauth---------***********-----------------**************------------")
            m_sender = "Guest"
            m_message_form = MessageToServiceForm(initial={
                'default_aka': m_sender,
            })
            print("print form inside the try---------***********-----------------**************------------")
            print(m_message_form)
        except UserProfile.DoesNotExist:
            print("inside of try except---------***********-----------------**************------------")
            order_form = OrderForm()

    # messages_to_service = profile.orders.all()
    service = profile
    all_messages = ContactMessage.objects.all()
    template = 'contact_services/contact_service.html'
    context = {
        'service': service,
        'form': form,
        'all_messages': all_messages,
        # 'on_profile_page': True
    }
    return render(request, template, context)

def delete_service_message(request, message_id, username):
    """ Delete a product from the store """
    username = username
    template = 'contact_services/contact_service.html'
    message_to_del = get_object_or_404(ContactMessage, pk=message_id)
    message_to_del.delete()
    messages.success(request, 'Message deleted!')
    return redirect(reverse('contact_service', args=[username]))
