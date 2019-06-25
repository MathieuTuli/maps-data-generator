import pytest

from mapsdg.components import ImageShape


def test_image_shape():
    try:
        img_shape = ImageShape(w=100, h=100)
        if img_shape.w != 100 or img_shape.h != 100:
            pytest.fail()
    except Exception:
        pytest.fail()
    for i in [-1, 0]:
        try:
            img_shape = ImageShape(w=i, h=100)
            if img_shape.w != i or img_shape.h != 100:
                pytest.fail()
        except ValueError:
            pass
        except Exception:
            pytest.fail()
    for i in [-1, 0]:
        try:
            img_shape = ImageShape(w=100, h=i)
            if img_shape.w != 100 or img_shape.h != i:
                pytest.fail()
        except ValueError:
            pass
        except Exception:
            pytest.fail()
