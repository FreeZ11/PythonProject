from django import forms
from .models import Channel


class ChannelForm(forms.ModelForm):

    class Meta:
        model = Channel
        fields = [
            'name',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'channel_name'})
        }


