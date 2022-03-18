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
    user_profile = get_object_or_404(UserProfile, user=request.user)
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
        my_profile_form = UserMyProfileForm(request.POST, instance=user_profile)
        if my_profile_form.is_valid():
            my_profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))

    my_profile_form = UserMyProfileForm(instance=user_profile)
    orders = OrderedMessages.objects.filter(s_contact_message__m_sender=user_profile)
    message_history = ContactMessage.objects.filter(m_receiver=user_profile,m_sender=user_profile)
    template = 'profiles/profile.html'
    context = {
        'my_profile_form': my_profile_form,
        'orders': orders,
        'on_profile_page': True,
        'all_messages': message_history,
        'user_profile': user_profile
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