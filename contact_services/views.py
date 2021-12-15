from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from profiles.models import UserProfile
from .models import ContactMessage
from .forms import MessageToServiceForm
import gc
# import pprint as pp


def contact_service(request, username):
    """ Display the user's profile. """
    print("inside contact_service---------***********-----------------**************------------")
    print(username)
    profile = get_object_or_404(UserProfile, default_aka=username)
    # profile=admin1 = user loggedin
    # type= class = <class 'profiles.models.UserProfile'>

    if request.method == 'POST':
        form = MessageToServiceForm(request.POST)
        print("below form inside of post ---------***********-----------------**************------------")

        if form.is_valid():
            form.save()
            print("new_message from view contact_service ---------***********-----------------**************------------")
            messages.success(request, 'Message updated successfully')
        else:
            print("above error message form is not valid ---------***********-----------------**************------------")
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
# what the heck the next two lines are doing???
    print("before calling form on view---------***********-----------------**************------------")
    form = MessageToServiceForm()
    print(form)
    print("after calling form on view---------***********-----------------**************------------")

    # messages_to_service = profile.orders.all()
    service = profile
    template = 'contact_services/contact_service.html'
    context = {
        'service': service,
        'form': form,
        # 'orders': orders,
        # 'on_profile_page': True
    }

    return render(request, template, context)

# ???after adding the on_profile_page, go to toast to finalize it. This is for a message to let people know that the profiles was successfully changed
    # print("request---------***********-----------------**************------------")
    # print(request)
    # print("template---------***********-----------------**************------------")
    # print(template)
    # print(" context---------***********-----------------**************------------")
    # print(context)
    # print("ContactMessage.objects.all---------***********-----------------**************------------")
    
    # classcm = ContactMessage.objects.all()
    # print(classcm)
    # print("dir()---------***********-----------------**************------------")
    # classcm1 = dir()
    # print(classcm1)
    # print("dir(classcm)---------***********-----------------**************------------")
    # classcm = dir(classcm)
    # print(classcm)
    # print("list __dir__---------***********-----------------**************------------")  
    # listdir = classcm.__dir__
    # print(listdir)

    # # print("vars()---------***********-----------------**************------------")
    # # classcm = vars(classcm)
    # # print(classcm)
    
    # print("ContactMessage.objects.filter---------***********-----------------**************------------")
    # classobjid = ContactMessage.objects.filter(id=10)
    # print(classobjid)
    
    # print("list all---------***********-----------------**************------------")
    # listall = list(classcm)
    # print(listall)
    
    # # print("list pp.pprint(dict(os.environ))---------***********-----------------**************------------")
    # # listdir = pp.pprint(dict(classcm))
    # # print(listdir)