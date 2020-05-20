from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse
import urllib.request
import json
# Create your views here.
from .forms import ChannelForm
from .models import Channel
from django.views import View
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


class home_view(View):
    template_name = 'index.html'

    def get(self, request):
        form = ChannelForm(request.GET)
        channels = Channel.objects.last()
        context = {'form': form, 'channels': channels}
        return render(request, self.template_name, context)

    def post(self, request):
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
            get_data(text)
            return redirect('home')
        else:
            return redirect('home')


def get_data(request, *args, **kwargs):
    values = [360, 420, 2000, 50000]
    labels = ["Views", "Views","Views","Views"]
    data = {
        "values": values,
        "labels": labels,
    }
    return JsonResponse(data)
