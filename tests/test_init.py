import importlib.resources

from mapsdg.google_maps_api import GoogleMapsAPI
from mapsdg.components import ViewType
import mapsdg.utils
import pytest


API_KEY = importlib.resources.read_text('mapsdg', '.api_key')
GAPI = GoogleMapsAPI(API_KEY)


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_download_from_url():
    url = GAPI.get_image_url(addr='233 soper place, ottawa, ontario, canada',
                             view_type=ViewType.staticmap)
    img = mapsdg.utils.get_image_from_url(url)
    fail_if(img is None)
    fail_if(img.shape != (400, 640, 4))
    img = mapsdg.utils.get_image_from_url(0)
    fail_if(img is not None)
