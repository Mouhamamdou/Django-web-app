from django import forms
from review.models import Review
from django.core.exceptions import ValidationError


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Review
        fields = ['ticket', 'rating', 'headline', 'body']

    def clean_ticket(self):
        ticket = self.cleaned_data.get('ticket')
        if self.instance.pk:
            if Review.objects.filter(ticket=ticket).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Une critique a déjà été postée pour ce ticket.")
        else:
            if Review.objects.filter(ticket=ticket).exists():
                raise forms.ValidationError("Une critique a déjà été postée pour ce ticket.")
        return ticket
