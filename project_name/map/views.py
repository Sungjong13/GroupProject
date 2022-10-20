from django.shortcuts import render
from pathlib import Path
import os
import json
from django.core.exceptions import ImproperlyConfigured


def get_secret(setting,secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

# Create your views here.
def map_window(request):
    # get kakao api key
    BASE_DIR = Path(__file__).resolve().parent.parent
    secret_file = os.path.join(BASE_DIR, 'secrets.json')
    with open(secret_file) as f:
        secrets = json.loads(f.read())
    KAKAO_API_KEY = get_secret("KAKAO_API_KEY",secrets)

    return render(request, 'map/map_window.html', {"KAKAO_API_KEY":KAKAO_API_KEY})



