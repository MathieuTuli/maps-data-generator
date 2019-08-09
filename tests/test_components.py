import pytest

from mapsdg.components import GeocodedLocation, ImageShape, StaticMapType, \
    ImageFormat, LatLon, ViewType, Heading, FieldOfView, Pitch, Radius


def fail_if(boolean):
    if boolean:
        pytest.fail()


def test_heading():
    heading = Heading()
    fail_if(heading.value != 0)

    try:
        Heading(-361)
        pytest.fail()
    except ValueError:
        pass
    try:
        Heading(361)
        pytest.fail()
    except ValueError:
        pass

    fail_if(Heading(200).value != 200)
    fail_if(Heading(-200).value != -200)


def test_field_of_fiew():
    fov = FieldOfView()
    fail_if(fov.value != 90)

    try:
        FieldOfView(-1)
        pytest.fail()
    except ValueError:
        pass
    try:
        FieldOfView(361)
        pytest.fail()
    except ValueError:
        pass

    fail_if(FieldOfView(10).value != 10)


def test_pitch():
    pitch = Pitch()
    fail_if(pitch.value != 0)

    try:
        Pitch(-100)
        pytest.fail()
    except ValueError:
        pass
    try:
        Pitch(361)
        pytest.fail()
    except ValueError:
        pass

    fail_if(Pitch(10).value != 10)
    fail_if(Pitch(-10).value != -10)


def test_radius():
    radius = Radius()
    fail_if(radius.value != 50)

    try:
        Radius(-100)
        pytest.fail()
    except ValueError:
        pass

    fail_if(Radius(10).value != 10)


def test_image_shape():
    try:
        img_shape = ImageShape(width=100, height=100)
        fail_if(img_shape.width != 100 or img_shape.height != 100)
    except Exception:
        pytest.fail()
    for i in [-1, 0]:
        try:
            img_shape = ImageShape(width=i, height=100)
            fail_if(img_shape.width != i or img_shape.height != 100)
        except ValueError:
            pass
        except Exception:
            pytest.fail()
    for i in [-1, 0]:
        try:
            img_shape = ImageShape(width=100, height=i)
            fail_if(img_shape.width != 100 or img_shape.height != i)
        except ValueError:
            pass
        except Exception:
            pytest.fail()


def test_lat_lon():
    x = LatLon(lon=100, lat=200)
    fail_if(x.lon != 100)
    fail_if(x.lat != 200)
