import urllib.request
import json


def get_data(name):
    """Get info about YT channel, and return dictionary."""

    key = "AIzaSyCGpvMVtDdvBVboHjxRDsWdx4wXTkQPf_0"
    data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + name + "&key=" + key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    views = json.loads(data)["items"][0]["statistics"]["viewCount"]
    videos = json.loads(data)["items"][0]["statistics"]["videoCount"]
    data = {'subsriptions': int(subs), 'videos': int(videos), 'views': int(views)}
    return data


print(get_data("DisStream"))
