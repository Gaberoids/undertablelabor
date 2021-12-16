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
