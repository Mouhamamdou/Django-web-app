from django import forms
from ticket.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class TicketAndReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    headline = forms.CharField(max_length=128)
    body = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

