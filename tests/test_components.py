import pytest

from mapsdg.components import ImageShape


def fail_if(boolean):
    if boolean:
        pytest.fail()


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
