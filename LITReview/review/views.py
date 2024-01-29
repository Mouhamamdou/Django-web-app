from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Review
from .forms import ReviewForm
from ticket.views import UserIsOwnerMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ticket.models import Ticket
from django.shortcuts import redirect, get_object_or_404


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    # fields = ['ticket', 'rating', 'headline', 'body']
    form_class = ReviewForm
    template_name = 'review/review_form.html'
    success_url = reverse_lazy('review-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        ticket_id = self.kwargs.get('ticket_id')
        if ticket_id:
            initial['ticket'] = get_object_or_404(Ticket, id=ticket_id)
        return initial


class ReviewUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Review
    # fields = ['rating', 'headline', 'body']
    form_class = ReviewForm
    template_name = 'review/review_update_form.html'
    success_url = reverse_lazy('review-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        ticket_id = self.kwargs.get('ticket_id')
        if ticket_id:
            initial['ticket'] = get_object_or_404(Ticket, id=ticket_id)
        return initial


class ReviewDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Review
    template_name = 'review/review_confirm_delete.html'
    success_url = reverse_lazy('review-list')


class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'review/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    template_name = 'review/review_detail.html'

