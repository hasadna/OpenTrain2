from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Network
import json


# Create your views here.

def index(request):
    return JsonResponse({'result': "Hello, world. You're at the data index."})


@csrf_exempt
def submit_network(request):
    if request.method != 'POST':
        return JsonResponse({'details': 'not allowed'}, status=405)

    d = json.loads(request.body)
    bssid = d.get('bssid')
    name = d.get('name')
    Network.objects.create(bssid=bssid, name=name)

    return JsonResponse(data={'bssid': bssid, 'name': name}, status=201)


def network_list(request):
    networks = list(Network.objects.values('id', 'bssid', 'name'))
    response = JsonResponse(data=dict(networks=networks), safe=False)
    return response
