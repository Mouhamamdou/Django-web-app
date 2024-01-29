from django import forms
from django.contrib.auth import get_user_model
from userfollows.models import UserFollows


User = get_user_model()


class UserFollowsForm(forms.ModelForm):
    followed_username = forms.CharField(label="", max_length=150)

    class Meta:
        model = UserFollows
        fields = []

    def clean_followed_username(self):
        username = self.cleaned_data['followed_username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Cet utilisateur n'existe pas.")
        return user
