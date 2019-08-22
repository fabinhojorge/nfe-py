from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import base64
from django.conf import settings
from bs4 import BeautifulSoup
from .models import Nfe


@csrf_exempt
@api_view(['GET'])
def sync_v1(_):
    """This endpoint is responsible for sync XMLs of NFes from Arquivei. """

    url = settings.ARQUIVEI_ENDPOINT
    headers = settings.ARQUIVEI_HEADERS
    proxies = settings.ARQUIVEI_PROXIES
    timeout = settings.ARQUIVEI_TIMEOUT

    data = []

    while True:
        print(" --> Requesting: {0}".format(url))
        next_url = ''

        try:
            r = requests.get(url, headers=headers, proxies=proxies, timeout=timeout)
        except requests.exceptions.ReadTimeout:
            raise

        # [ ] CRIAR JOB DE EXECUÇÃO NO BACKGROUND PARA NÃO DAR TIMEOUT (module background_task)
        # [ ] CRIAR FLAG DE EXECUÇÃO no banco. Enquanto esta executando retornar para qualquer request futura que
        #   ja existe.
        # [ ] Save in the model
        # [ ] check if the access_key already exists, if yes: continue to the next NFE
        # [ ] Block try catch to return internal error when got a problem

        if r.status_code == 200:

            response = r.json()
            for i in range(len(response['data'])):
                response['data'][i]['xml'] = base64.b64decode(response['data'][i]['xml'])
                access_key = response['data'][i]['access_key']
                xml = response['data'][i]['xml']
                soup = BeautifulSoup(xml)
                value = soup.select('total ICMSTot vNF')[0].text
                print("VALOR: ", value)

            # data.append(response['data'])
            data.append(response)

            if 'page' in response.keys() and 'next' in response['page']:
                next_url = response['page']['next']

        if next_url == '' or next_url == url:
            break
        else:
            url = next_url

    return Response(data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def find_v1(_):
    return Response("{'find':'!!!!!'}")
