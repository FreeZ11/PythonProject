from django.shortcuts import render

from django.http import HttpResponse
import urllib.request
import json
# Create your views here.
from .forms import ChannelForm, RawChannelForm
from .models import Channel

# def home_view(request):
#     form = ChannelForm(request.POST)
#     text = ""
#     if form.is_valid():
#         text = form.cleaned_data
#         form = ChannelForm()
#     context = {'form': form, 'text': text}
#
#     return render(request, "index.html", context)


from django.views.generic import TemplateView


class home_view(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        text = ""

        def get_data(name):
            """Get info about YT channel, and return dictionary."""
            key = "AIzaSyCGpvMVtDdvBVboHjxRDsWdx4wXTkQPf_0"

            data = urllib.request.urlopen(
                "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + name + "&key=" + key).read()

            subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
            views = json.loads(data)["items"][0]["statistics"]["viewCount"]
            videos = json.loads(data)["items"][0]["statistics"]["videoCount"]
            data = {'name': name, 'subscriptions': int(subs), 'videos': int(videos), 'views': int(views)}
            Channel.objects.create(name=name, subscriptions=int(subs), videos=int(videos), views=int(views))
            return data

        form = ChannelForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['name']
            print(text)
            form = ChannelForm()
            print(get_data(text))
        context = {'form': form, 'text': text}

        return render(request, self.template_name, context)
