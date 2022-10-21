from django.shortcuts import render
from pathlib import Path
import os
import json
from django.core.exceptions import ImproperlyConfigured
import requests


def get_key(setting):
    '''
    returns kakao api key in secrets.json
    '''
    BASE_DIR = Path(__file__).resolve().parent.parent
    secret_file = os.path.join(BASE_DIR, 'secrets.json')
    with open(secret_file) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

def get_latlon(address):
    '''
    input string address, return latitude longitude as tuple.
    '''
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    api_key = get_key("JS_KEY")
    headers = {"Authorization": f"KakaoAK {api_key}"}
    api_json = json.loads(str(requests.get(url,headers=headers).text))
    if api_json['documents']:
        address = api_json['documents'][0]
    else:
        # error 값 2
        return(2,2)

    return (address['y'], address['x'])

# Create your views here.
def map_window(request):
    # get kakao api key
    KAKAO_API_KEY = get_key("KAKAO_API_KEY")

    # 사용자 입력 주소 처리
    if request.method == "POST":
        address = request.POST["address"]
        lat,lon = get_latlon(address)
    else:
        # default 값 1
        lat,lon = (1, 1)

    return render(request, 'map/map_window.html', {"KAKAO_API_KEY":KAKAO_API_KEY, "lat":lat, "lon":lon})

if __name__ == '__main__':
    pass
    get_latlon('대천로 103번길')


