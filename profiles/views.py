from django.shortcuts import render, get_object_or_404
from django.contrib import messages

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
    my_profile_form = ''

    if request.method == 'POST':
        # request.POST = <QueryDict: {'csrfmiddlewaretoken': ['kOsHMzYvgUgeOLyFPCGj0e0ZWhkbmbqgHBEgAMfMoooQWCYMvIXVNtezEv0YIxBe'], 'default_aka': ['serv1'], 'default_service_provider': ['true'], 'default_town_or_city': [''], 'default_county': [''], 'default_postcode': ['234523']}>
        my_profile_form = UserMyProfileForm(request.POST, instance=profile)
        if my_profile_form.is_valid():
            my_profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        # prepopulating the user field on the form to have the user authenticated
        if request.user.is_authenticated:
            print("user authenticated---------***********-----------------**************------------")
            try:
                print("inside of try user is authenticated---------***********-----------------**************------------")
                profile = UserProfile.objects.get(user=request.user)
                # profile has access to all fieldsrelated to a the user. Including the fileds from Contact_Message and UserProfile models because the key relationships between them
                my_profile_form = UserMyProfileForm(initial={
                    'default_aka': profile.user,
                    'default_service_provider': profile.default_service_provider,
                    'default_postcode': profile.default_postcode,
                    'default_town_or_city': profile.default_town_or_city,
                    'default_county': profile.default_county
                })
                print("print form inside the try---------***********-----------------**************------------")
                print(my_profile_form)
            except UserProfile.DoesNotExist:
                print("inside of try except---------***********-----------------**************------------")
                order_form = OrderForm()
        else:
            print("user not authenticated---------***********-----------------**************------------")

    form = UserMyProfileForm(instance=profile)
    # orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'my_profile_form': my_profile_form,
        # 'orders': orders,
        'on_profile_page': True
    }
    # after adding the on_profile_page, go to toast to finalize it. This is for a message to let people know that the profiles was successfully changed
    return render(request, template, context)


def all_services(request):
    services = UserProfile.objects.filter(default_service_provider=True)
    # <QuerySet [<UserProfile: admin1>, <UserProfile: Guest>, <UserProfile: user1>, <UserProfile: user4>]>    print(services)

    template = 'profiles/services.html'
    context = {
        'services': services,
    }

    return render(request, template, context)
