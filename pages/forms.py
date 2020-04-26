from django import forms
from .models import Channel


class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = [
            'name',
            'subscriptions',
            'videos',
            'views'
        ]


class RawChannelForm(forms.Form):
    name = forms.CharField()
    subscriptions = forms.DecimalField()
    videos = forms.DecimalField()
    views = forms.DecimalField()
