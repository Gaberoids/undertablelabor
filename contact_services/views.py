from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from profiles.models import UserProfile
from .models import ContactMessage
from .forms import MessageToServiceForm


def contact_service(request, username):
    """ Display the user's profile. """

    # profile = receiever
    profile = get_object_or_404(UserProfile, id=username)
    # profile=admin1 = user selected from list of services
    # type= class = <class 'profiles.models.UserProfile'>
    print("profile ---------***********-----------------**************------------")
    print(profile)

    print("dir(profile) ---------***********-----------------**************------------")
    print(dir(profile))

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
            # form authofill
            print("inside of try is auth---------***********-----------------**************------------")
            # m_profile = sender
            m_profile = UserProfile.objects.get(user=request.user)
            # print(m_profile.user.email)
            print("type(m_profile)---------***********-----------------**************------------")
            print(type(m_profile))
            print(m_profile.user.username)
            m_message_form = MessageToServiceForm(initial={
                'm_sender': m_profile,
                'm_receiver': profile,
                'm_sender_email': m_profile.user.email,
            })
            print("print form inside the try after form1---------***********-----------------**************------------")
            print(m_message_form)

            # filter all messages based on the user logged in and service provider profile
            # all_messages_per_profile = all_messages.objects.filter(m_receiver=)

        except UserProfile.DoesNotExist:
            print("inside of try except---------***********-----------------**************------------")
            order_form = OrderForm()
    else:
        print("user not authenticated---------***********-----------------**************------------")
        try:
            print("inside of try isnotauth---------***********-----------------**************------------")
            # Guest user id = 3
            m_sender_guest = UserProfile.objects.get(id=3)
            print("m_sender_guest ---------***********-----------------**************------------")
            print(type(m_sender_guest))
            print(m_sender_guest)
            
            m_message_form = MessageToServiceForm(initial={
                'm_sender': m_sender_guest,
                'm_receiver': profile,
            })
            print("print form inside the try---------***********-----------------**************------------")
            print(m_message_form)
        except UserProfile.DoesNotExist:
            print("inside of try except---------***********-----------------**************------------")
            order_form = OrderForm()
    
    

    # messages below place holderstween logged in user and service rpovider
    all_messages = ContactMessage.objects.all()
    for x in all_messages:
        print(x.m_title, x.m_body, x.m_sender, x.m_receiver)
 
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
