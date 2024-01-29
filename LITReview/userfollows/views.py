from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserFollowsForm
from .models import UserFollows
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages


class UserFollowCreateView(LoginRequiredMixin, CreateView, ListView):
    model = UserFollows
    form_class = UserFollowsForm
    template_name = 'userfollows/user_follows_form.html'
    success_url = reverse_lazy('user-follows-list')
    context_object_name = 'users_follow'

    def form_valid(self, form):
        followed_user = form.cleaned_data['followed_username']
        if followed_user == self.request.user:
            form.add_error(None, "Vous ne pouvez pas vous suivre vous-même.")
            return self.form_invalid(form)
        elif UserFollows.objects.filter(user=self.request.user, followed_user=followed_user).exists():
            form.add_error(None, "Vous suivez déjà cet utilisateur.")
            return self.form_invalid(form)
        else:
            form.instance.user = self.request.user
            form.instance.followed_user = followed_user
            response = super().form_valid(form)
            messages.success(self.request, f"Vous suivez maintenant {followed_user.username}.")
            return response

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})
    
    def get_queryset(self):
        user = self.request.user
        return UserFollows.objects.filter(user=user)


class UserFollowDeleteView(LoginRequiredMixin, DeleteView):
    model = UserFollows
    template_name = 'userfollows/user_follows_confirm_delete.html'
    success_url = reverse_lazy('user-follows-list')


class UserFollowListView(LoginRequiredMixin, ListView):
    model = UserFollows
    template_name = 'userfollows/user_follows_list.html'
    context_object_name = 'users_follow'

    def get_queryset(self):
        user = self.request.user
        return UserFollows.objects.filter(user=user)
