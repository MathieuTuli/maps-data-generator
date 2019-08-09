'''Components for typing purposes'''
# from dataclasses import dataclass
from typing import NamedTuple

import enum


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


StaticMapType = enum.Enum(
    'StaticMapType', ['roadmap', 'satellite', 'hybrid', 'terrain'])


ImageFormat = enum.Enum(
    'ImageFormat', ['png', 'png8', 'png32', 'gif', 'jpg', 'jpg-baseline'])


class LatLon(NamedTuple):
    lon: str
    lat: str


__all__ = "GeocodedLocation", "ImageShape", "StaticMapType", "ImageShape",\
    "LatLon"
