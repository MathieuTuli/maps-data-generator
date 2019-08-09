'''Components for typing purposes'''
# from dataclasses import dataclass
from typing import NamedTuple

import enum


class Heading:
    def __init__(self, heading: int = 0):
        try:
            heading = int(heading)
            if heading > 360 or heading < -360:
                raise
            self.value = heading
        except Exception:
            raise ValueError(
                "Incorrect heading value. Must be an int >= 0, <= 360")


class FieldOfView:
    def __init__(self, fov: int = 90):
        try:
            fov = int(fov)
            if fov > 120 or fov < 0:
                raise
            self.value = fov
        except Exception:
            raise ValueError(
                "Incorrect field of view value. Must be an int >= 0, <= 120")


class Pitch:
    def __init__(self, pitch: int = 0):
        try:
            pitch = int(pitch)
            if pitch > 90 or pitch < -90:
                raise
            self.value = pitch
        except Exception:
            raise ValueError(
                "Incorrect pitch value. Must be an int >= -90, <= 90")


class Radius:
    def __init__(self, radius: int = 50):
        try:
            radius = int(radius)
            if radius < 0:
                raise
            self.value = radius
        except Exception:
            raise ValueError(
                "Incorrect radius value. Must be an int >= 0")


class GeocodedLocation(NamedTuple):
    ne_lat: float
    ne_lon: float
    sw_lat: float
    sw_lon: float
    lat: float
    lon: float
    original_address: str


class ImageShape(NamedTuple):
    width: int
    height: int


ViewType = enum.Enum(
    'ViewType', ['streetview', 'staticmap'])

StaticMapType = enum.Enum(
    'StaticMapType', ['roadmap', 'satellite', 'hybrid', 'terrain'])


ImageFormat = enum.Enum(
    'ImageFormat', ['png', 'png8', 'png32', 'gif', 'jpg', 'jpg-baseline'])


class LatLon(NamedTuple):
    lon: str
    lat: str


__all__ = "GeocodedLocation", "ImageShape", "StaticMapType", "ImageShape",
"LatLon"
