from itertools import chain
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Ticket
from userfollows.models import UserFollows
from review.models import Review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.exceptions import PermissionDenied
from .forms import TicketAndReviewForm, TicketForm


class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class TicketAndReviewCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketAndReviewForm
    template_name = 'ticket/ticket_and_review_form.html'
    success_url = reverse_lazy('ticket-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        ticket = form.save(commit=False)
        ticket.save()

        Review.objects.create(
            ticket=ticket,
            user=self.request.user,
            rating=form.cleaned_data['rating'],
            headline=form.cleaned_data['headline'],
            body=form.cleaned_data['body']
        )
        return super().form_valid(form)


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    # fields = ['title', 'description', 'image']
    form_class = TicketForm
    template_name = 'ticket/ticket_form.html'
    success_url = reverse_lazy('ticket-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TicketUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Ticket
    # fields = ['title', 'description', 'image']
    form_class = TicketForm
    template_name = 'ticket/ticket_update_form.html'
    success_url = reverse_lazy('ticket-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TicketDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Ticket
    template_name = 'ticket/ticket_confirm_delete.html'
    success_url = reverse_lazy('ticket-list')


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'ticket/ticket_list.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)


class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'ticket/ticket_detail.html'


class Home(LoginRequiredMixin, ListView):
    template_name = "ticket/home.html"
    context_object_name = 'tickets_and_reviews'
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        followed_users = UserFollows.objects.filter(user=user).values_list('followed_user', flat=True)

        tickets = Ticket.objects.filter(Q(user__in=followed_users) | Q(user=user))
        reviews = Review.objects.filter(Q(user__in=followed_users) | Q(user=user) | Q(ticket__user=user))

        tickets_and_reviews = sorted(
            list(chain(tickets, reviews)),
            key=lambda instance: instance.time_created,
            reverse=True
        )
        return tickets_and_reviews

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['range_5'] = range(1, 6)
        return context


