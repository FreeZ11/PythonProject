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
valuesSubs = []


class home_view(View):
    template_name = 'index.html'

    def data_getter(self, channel):
        channel_set = Channel.objects.filter(name=channel)
        subs = []
        views = []
        for p in channel_set:
            subs.append(int(p.subscriptions))
            views.append(int(p.views))
        views_growth = [views[i] - views[i - 1] for i in range(1, len(views))]
        return views_growth[-10:-1], subs[-10:-1]

    def get(self, request):
        global values
        global valuesSubs
        form = ChannelForm(request.GET)
        channels = Channel.objects.last()
        if "1st" in request.GET:
            values, valuesSubs = self.data_getter("PewDiePie")

        elif "2nd" in request.GET:
            values, valuesSubs = self.data_getter("liebner12")

        elif "3rd" in request.GET:
            values, valuesSubs = self.data_getter("UFC")

        elif "4th" in request.GET:
            values, valuesSubs = self.data_getter("DisStream")

        elif "5th" in request.GET:
            values, valuesSubs = self.data_getter("Nervarien")

        elif "6th" in request.GET:
            values, valuesSubs = self.data_getter("mietczynski")

        elif "7th" in request.GET:
            values, valuesSubs = self.data_getter("Nightblue3")

        elif "8th" in request.GET:
            values, valuesSubs = self.data_getter("OwcaWK")

        elif "9th" in request.GET:
            values, valuesSubs = self.data_getter("BadzmyPowazni")

        elif "10th" in request.GET:
            values, valuesSubs = self.data_getter("KSW")

        context = {'form': form, 'channels': channels}
        return render(request, self.template_name, context)

    def post(self, request):
        # def get_data(name):
        #     """Get info about YT channel, and return dictionary."""
        #     key = "AIzaSyCGpvMVtDdvBVboHjxRDsWdx4wXTkQPf_0"
        #
        #     data = urllib.request.urlopen(
        #         "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + name + "&key=" + key).read()
        #
        #     subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        #     views = json.loads(data)["items"][0]["statistics"]["viewCount"]
        #     videos = json.loads(data)["items"][0]["statistics"]["videoCount"]
        #     data = {'name': name, 'subscriptions': int(subs), 'videos': int(videos), 'views': int(views)}
        #     Channel.objects.create(name=name, subscriptions=int(subs), videos=int(videos), views=int(views))
        #     return data

        form = ChannelForm(request.POST)
        if form.is_valid():
            # text = form.cleaned_data['name']
            # get_data(text)
            return redirect('home')
        else:
            return redirect('home')


def get_data(request, *args, **kwargs):
    global values
    global valuesSubs
    prediction = predict_next_value(values)
    predictionSubs = predict_next_value(valuesSubs)
    values = prediction[0]
    valuesSubs = predictionSubs[0]
    labels = prediction[1]
    data = {
        "values": values,
        "valuesSubs": valuesSubs,
        "labels": labels,
    }
    return JsonResponse(data)
