from django.shortcuts import render
from pathlib import Path
import os
import json
from django.core.exceptions import ImproperlyConfigured
import requests
from django.http import JsonResponse

# 저장된 두가지 kakao api키 적용
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

# 입력받은 주소 (도로명 or 지명) 위도경도로 반환
def get_latlon(address):
    '''
    input string address, return latitude longitude as tuple.
    '''
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    api_key = get_key("JS_KEY")
    headers = {"Authorization": f"KakaoAK {api_key}"}
    api_json = json.loads(str(requests.get(url,headers=headers).text))
    if api_json['documents']:
        info = api_json['documents'][0]
        return (info['y'], info['x'])
    else:
        # error 값 2 : 인식 못하는 주솟값 입력함.
        return(2,2)

# map 메인화면
def map_window(request):
    # get kakao api key
    KAKAO_API_KEY = get_key("KAKAO_API_KEY")
    
    return render(request, 'map/map_window.html', {"KAKAO_API_KEY":KAKAO_API_KEY})


# 이동 누를때 jsonresponse
def map_update(request):
    address = request.POST.get("address")
    lat,lon = get_latlon(address)

    return JsonResponse({"lat":lat,"lon":lon})


if __name__ == '__main__':
    pass


