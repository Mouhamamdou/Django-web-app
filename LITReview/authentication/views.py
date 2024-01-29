from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from . import forms


class SignupPageView(CreateView):
    form_class = forms.SignupForm
    template_name = 'authentication/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # return redirect(self.get_success_url())
        return redirect('home')
