from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from django.conf import settings
from .models import Nfe
from .serializers import NfeSerializer


@csrf_exempt
@api_view(['GET'])
def nfe_sync_v1(_):
    """This endpoint is responsible for sync the NFE's xmls from Arquivei API."""

    data = {'status': {'code': '200', 'message': 'Ok', }, 'data': []}
    url = settings.ARQUIVEI_ENDPOINT

    while True:
        next_url = ''
        data_arquivei = {'url': url, 'endpoint_status': {'code': '200', 'message': 'Ok', }, 'endpoint_data': []}

        try:
            r = requests.get(url, headers=settings.ARQUIVEI_HEADERS, proxies=settings.ARQUIVEI_PROXIES,
                             timeout=settings.ARQUIVEI_TIMEOUT, )
            r_status = {'code': str(r.status_code), 'message': 'Ok', }
        except requests.exceptions.ReadTimeout:
            r = None
            r_status = {'code': status.HTTP_504_GATEWAY_TIMEOUT,
                        'message': 'Time out while trying to reach the Arquivei Endpoint.', }
        except Exception:
            r = None
            r_status = {'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': 'Failed to request the Arquivei Endpoint.', }
        finally:
            data_arquivei['endpoint_status'] = r_status

        if r is not None and r.status_code == 200:
            response = r.json()

            if 'data' in response.keys():
                for i in range(len(response['data'])):
                    if 'access_key' in response['data'][i].keys() and 'xml' in response['data'][i].keys():
                        resp_inst = Nfe.prepare_nfe_and_save(response['data'][i])
                        data_arquivei['endpoint_data'].append(resp_inst)

            if 'page' in response.keys() and 'next' in response['page']:
                next_url = response['page']['next']

        data['data'].append(data_arquivei)

        if next_url == '' or next_url == url:
            break
        else:
            url = next_url

    return Response(data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def nfe_find_v1(_, access_key):
    """This endpoint is to fetch in local database the already synchronized NFEs."""

    try:
        nfe = Nfe.objects.get(access_key=access_key)
        nfe_serializer = NfeSerializer(nfe)
        data = dict()
        data['status'] = {'code': '200', 'message': 'Ok', }
        data['data'] = nfe_serializer.data
        return Response(data, status=status.HTTP_200_OK)
    except Nfe.DoesNotExist:
        data = dict()
        if len(Nfe.objects.all()) == 0:
            data['status'] = {'code': '404', 'message': 'The local database is empty. Please sync first.', }
        else:
            data['status'] = {'code': '404', 'message': 'Access key not found', }
        return Response(data, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def custom404(_, exception=None):
    """Custom 404 page"""
    data = dict()
    data['status'] = {'code': '404', 'message': 'Page not Found', }
    return Response(data, status=status.HTTP_404_NOT_FOUND)
