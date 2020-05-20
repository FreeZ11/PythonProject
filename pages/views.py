from django.shortcuts import render, redirect
from predict import predict_next_value
from django.http import JsonResponse
import urllib.request
import json
# Create your views here.
from .forms import ChannelForm
from .models import Channel
from django.views import View

values = []


class home_view(View):
    template_name = 'index.html'

    def get(self, request):
        global values
        form = ChannelForm(request.GET)
        channels = Channel.objects.last()
        if "1st" in request.GET:
            values = [-33, 3, 50, 123, -42, 120, 31, -23, 41]
        elif "2nd" in request.GET:
            values = [-33, 16, 50, 123, -42, 120, 31, -23, 41]
        elif "3rd" in request.GET:
            values = [-33, 100, 50, 123, -42, 120, 31, -23, 41]
        elif "4th" in request.GET:
            values = [-33, 100, 50, 123, -42, 120, 31, -23, 41]
        elif "5th" in request.GET:
            values = [-33, 200, 50, 123, -42, 120, 31, -23, 41]
        elif "6th" in request.GET:
            values = [-33, 53, 50, 123, -42, 120, 31, -23, 41]
        elif "7th" in request.GET:
            values = [-33, 69, 50, 123, -42, 120, 31, -23, 41]
        elif "8th" in request.GET:
            values = [-33, 23, 50, 123, -42, 120, 31, -23, 41]
        elif "9th" in request.GET:
            values = [-33, 420, 50, 123, -42, 120, 31, -23, 41]
        elif "10th" in request.GET:
            values = [-33, 360, 50, 123, -42, 120, 31, -23, 41]
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
    global values
    prediction = predict_next_value(values)
    values = prediction[0]
    labels = prediction[1]
    data = {
        "values": values,
        "labels": labels,
    }
    return JsonResponse(data)
