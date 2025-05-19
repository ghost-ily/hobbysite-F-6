from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import Profile
from .forms import ProfileForm

@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_form.html'
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

    def get_object(self, queryset=None):
        profile = get_object_or_404(Profile, user__username=self.kwargs['username'])
        if self.request.user != profile.user:
            raise PermissionDenied
        return profile

    def get_success_url(self):
        return reverse_lazy('user_management:profile-update', kwargs={'username': self.object.user.username})