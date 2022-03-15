from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from contact_services.models import ContactMessage
from checkout.models import OrderedMessages

# Create your views here.
from .models import UserProfile
from .forms import UserMyProfileForm

# from checkout.models import Order

# Create your views here.
def my_profile(request):
    """ Display the user's profile. """
    # reuqest = <WSGIRequest: GET '/profile/'>
    profile = get_object_or_404(UserProfile, user=request.user)
    # profile=admin1 = user loggedin
    # type= class = <class 'profiles.models.UserProfile'>
    # attributes_of_profile = [item for item in accounts if item.get('id')==10][]
    # my_profile_form = ''

    if request.method == 'POST':
        # request.POST = <QueryDict: {'csrfmiddlewaretoken': 
        # ...['kOsHMzYvgUgeOLyFPCGj0e0ZWhkbmbqgHBEgAMfMoooQWCYMvIXVNtezEv0YIxBe'],
        # ... 'default_aka': ['serv1'], 'default_service_provider': ['true'],
        # ...'default_town_or_city': [''], 'default_county': [''],
        # ... 'default_postcode': ['234523']}>
        my_profile_form = UserMyProfileForm(request.POST, instance=profile)
        if my_profile_form.is_valid():
            my_profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))

    my_profile_form = UserMyProfileForm(instance=profile)
    # orders = OrderedMessages.objects.filter(s_contact_message__m_sender=profile)
    # print(orders)
    # print("orders ---------***********-----------------**************------------")
    orders = OrderedMessages.objects.all()
    # for order in orders:
    #     order_id = order.s_contact_message
    #     print(order_id)
    #     print('order id above')
    #     contact_message = ContactMessage.objects.get(id=order_id)
    #     print(contact_message)
    #     print('contact message above')
    #     contact_message_sender_name = contact_message.contact_message_sender_name
    #     print(contact_message_sender_name)
    #     print("contact_message_sender_name above ---------***********-----------------**************------------")
    message_history = ContactMessage.objects.filter(m_receiver=profile,m_sender=profile)
    template = 'profiles/profile.html'
    context = {
        'my_profile_form': my_profile_form,
        'orders': orders,
        'on_profile_page': True,
        'all_messages': message_history
    }
    # after adding the on_profile_page, go to toast to finalize it. This is for a message to let people know that the profiles was successfully changed
    return render(request, template, context)


def all_services(request):
    services = UserProfile.objects.filter(default_service_provider=True)
    # <QuerySet [<UserProfile: admin1>, <UserProfile: Guest>, 
    # ...<UserProfile: user1>, <UserProfile: user4>]> print(services)

    template = 'profiles/services.html'
    context = {
        'services': services,
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