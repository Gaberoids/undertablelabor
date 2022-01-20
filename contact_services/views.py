from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from profiles.models import UserProfile
from .models import ContactMessage
from .forms import MessageToServiceForm


def contact_service(request, username):
    """ Display the user's profile. """

    # profile = receiever not loggedin
    profile = get_object_or_404(UserProfile, id=username)
    # profile=admin1 = user selected from list of services
    # type= class = <class 'profiles.models.UserProfile'>
    
    # messages below place holderstween logged in user and service rpovider
    all_messages = ContactMessage.objects.all()
    # print(" for loop all messages to get the table value ---------***********-----------------**************------------")
    # for x in all_messages:
    #     print(x.m_title, x.m_body, x.m_sender, x.m_receiver)

    # prepopulate m_sender and m_receiver
    if request.user.is_authenticated:
        print("user authenticated---------***********-----------------**************------------")
        try:
            # form authofill
            print("inside of try is auth---------***********-----------------**************------------")
            # user authenticated is m_profile
            m_profile = UserProfile.objects.get(user=request.user)
            # m_profile printed is <class 'profiles.models.UserProfile'>
            # m_profile.user.username printed is 'user1'
            m_message_form = MessageToServiceForm(initial={
                'm_sender': m_profile,
                'm_receiver': profile,
                'm_sender_email': m_profile.user.email,
            })
            # m_message_form printed is the html form you see on the page.

            # filter all messages based on the user logged in and service provider profile
            all_messages = ContactMessage.objects.filter(m_receiver=profile,m_sender=m_profile)

        except UserProfile.DoesNotExist:
            print("inside of try except---------***********-----------------**************------------")
            order_form = OrderForm()
    else:
        print("user not authenticated---------***********-----------------**************------------")
        try:
            print("inside of try isnotauth---------***********-----------------**************------------")
            # Guest user id = 3
            m_sender_guest = UserProfile.objects.get(id=3)
            # m_sender_guest printed is 'Guest'
            
            m_message_form = MessageToServiceForm(initial={
                'm_sender': m_sender_guest,
                'm_receiver': profile,
            })
            # m_message_form printed is the html form you see on the page.

        except UserProfile.DoesNotExist:
            print("inside of try except---------***********-----------------**************------------")
            order_form = OrderForm()
     
    service = profile
    template = 'contact_services/contact_service.html'
    context = {
        'service': service,
        'form': m_message_form,
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
