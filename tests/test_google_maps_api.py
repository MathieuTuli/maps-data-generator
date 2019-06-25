import importlib.resources

from mapsdg.google_maps_api import GoogleMapsAPI

API_KEY = importlib.resources.read_text('mapsdg', '.api_key')


def test_get_static_map():
    return
