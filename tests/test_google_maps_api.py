import importlib.resources
import pytest


from mapsdg.google_maps_api import GoogleMapsAPI
from mapsdg.components import GeocodedLocation, ImageShape, StaticMapType, \
    ImageFormat, LatLon, ViewType, Heading, FieldOfView, Pitch, Radius

API_KEY = importlib.resources.read_text('mapsdg', '.api_key')
GAPI = GoogleMapsAPI(API_KEY)


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_geocode_address():
    global GAPI


def test_get_static_map():
    global GAPI
    geocoded = GAPI.geocode_address('233 Soper Place, Ottawa, Ontario, Canada')
    url = GAPI.get_image_url(
        addr='233 Soper Place, Ottawa, Ontario, Canada',
        view_type=ViewType.staticmap,)

    expected_url = (
        f"https://maps.googleapis.com/maps/api/staticmap?" +
        f"center={geocoded.lat},{geocoded.lon}&" +
        f"zoom=20&" +
        f"size=640x400&" +
        f"maptype=satellite&" +
        f"format=png&" +
        "style=feature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff&" +
        f"key={API_KEY}".strip())

    fail_if(url != expected_url)
