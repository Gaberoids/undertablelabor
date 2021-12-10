from django.shortcuts import render

# from .models import UserProfile
# from .forms import UserProfileForm

def contact_service(request):
    """ Display the user's profile. """
    # profile = get_object_or_404(UserProfile, user=request.user)

    # if request.method == 'POST':
    #     form = UserProfileForm(request.POST, instance=profile)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Profile updated successfully')
    #     else:
    #         messages.error(request,
    #                        ('Update failed. Please ensure '
    #                         'the form is valid.'))
# what the heck the next two lines are doing???
    # form = UserProfileForm(instance=profile)
    # orders = profile.orders.all()

    template = 'contact_services/contact_service.html'
    # context = {
    #     # 'form': form,
    #     # 'orders': orders,
    #     # 'on_profile_page': True
    # }
    # after adding the on_profile_page, go to toast to finalize it. This is for a message to let people know that the profiles was successfully changed

    return render(request, template)
