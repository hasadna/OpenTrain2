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
    try:
        d = json.loads(request.body.decode('utf-8'))
    except ValueError as e:
        return JsonResponse({'details': str(e)}, status=400)
    bssid = d.get('bssid')
    name = d.get('name')
    if bssid is None or name is None:
        return JsonResponse({'details': 'bssid and name are mandatory'}, status=400)

    Network.objects.create(bssid=bssid, name=name)

    return JsonResponse(data={'bssid': bssid, 'name': name}, status=201)


def network_list(request):
    networks = list(Network.objects.values('id', 'bssid', 'name'))
    response = JsonResponse(data=dict(networks=networks), safe=False)
    return response
