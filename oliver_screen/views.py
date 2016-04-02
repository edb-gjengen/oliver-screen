from django.http import JsonResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'public/index.html'


# Mock views
def dummy_get_last_track(request):
    track = {'artist': 'The Album Leaf', 'title': 'Another Day (Revised)', 'time_since': '10 seconds'}
    return JsonResponse(track)


def dummy_now_playing(request):
    track = {
        'artist': 'The Album Leaf',
        'title': 'Over The Pond',
        'image': 'http://userserve-ak.last.fm/serve/_/2857325/The+Album+Leaf+1155442304.jpg',
        "video": ''
    }

    return JsonResponse({'track': track})
