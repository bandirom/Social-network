from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import ImageFileUploadForm, ChangePassForm, ProfileForm
from .models import Profile


def image_upload_ajax(request, user):
    profile = request.user.profile
    if request.method == 'POST':
        form = ImageFileUploadForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
        else:
            return JsonResponse({'error': True, 'errors': form.errors})


def headline(text, /, border="♦", *, width=50):
    return f" {text} ".center(width, border)


class ProfileView(View):
    template_name = 'app/profile.html'
    context_object_name = 'profile'

    def get(self, request, user=None, *args, **kwargs):
        # headline("request", "=")
        # print(request)
        profile = get_object_or_404(User, username=user)
        upload_image_form = ImageFileUploadForm()
        change_password = ChangePassForm()
        profile_form = ProfileForm()
        return render(request, 'account/profile.html', {'user_profile': profile,
                                                        'upload_image_form': upload_image_form,
                                                        'change_password': change_password,
                                                        'profile_form': profile_form,
                                                        })

    # def post(self, request, user=None, *args, **kwargs):
    #     headline("request", "=")
    #     print(request)
    #     print('user', user)


@login_required
def user_profile(request, user):
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'app/profile.html', {'profile': profile})