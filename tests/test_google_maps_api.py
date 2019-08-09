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


def test_api():
    try:
        GoogleMapsAPI(1)
        pytest.fail()
    except ValueError:
        pass


def test_geocode_address():
    global GAPI
    result = GAPI.geocode_address('non')
    fail_if(result is not None)
    try:
        GAPI.geocode_address('233 soper place, ottawa, ontario, canada')
    except Exception:
        pytest.fail()
    try:
        GAPI.geocode_address(0)
        pytest.fail()
    except Exception:
        pass


def test_get_static_center_string():
    result = GAPI.get_static_center_string('233 soper place')
    fail_if(not isinstance(result, str))

    try:
        GAPI.get_static_center_string(9)
    except Exception:
        pass


def test_get_static_map():
    global GAPI
    geocoded = GAPI.geocode_address('233 Soper Place, Ottawa, Ontario, Canada')

    try:
        url = GAPI.get_image_url(
            addr='233 Soper Place, Ottawa, Ontario, Canada',
            view_type=ViewType.staticmap,
            additional_parameters='key=stuff')
        pytest.fail()
    except ValueError:
        pass

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

    print(url)
    print(expected_url)
    fail_if(url != expected_url)


def test_get_street_view():
    global GAPI
    geocoded = GAPI.geocode_address('233 Soper Place, Ottawa, Ontario, Canada')
    url = GAPI.get_image_url(
        addr='233 Soper Place, Ottawa, Ontario, Canada',
        view_type=ViewType.streetview,)

    expected_url = (
        f"https://maps.googleapis.com/maps/api/streetview?" +
        f"location={geocoded.lat},{geocoded.lon}&" +
        f"heading=0&" +
        f"size=640x400&" +
        f"fov=90&" +
        f"pitch=0&" +
        f"radius=50&" +
        f"format=png&" +
        "style=feature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff&" +
        f"key={API_KEY}".strip())

    print(url)
    print(expected_url)
    fail_if(url != expected_url)

    url = GAPI.get_image_url(
        addr='233 Soper Place, Ottawa, Ontario, Canada',
        view_type=ViewType.streetview,
        heading=Heading(-45))

    expected_url = (
        f"https://maps.googleapis.com/maps/api/streetview?" +
        f"location={geocoded.lat},{geocoded.lon}&" +
        f"heading=-45&" +
        f"size=640x400&" +
        f"fov=90&" +
        f"pitch=0&" +
        f"radius=50&" +
        f"format=png&" +
        "style=feature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff&" +
        f"key={API_KEY}".strip())
    fail_if(url != expected_url)
    print(url)
    print(expected_url)
