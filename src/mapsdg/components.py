'''Components for typing purposes'''
# from dataclasses import dataclass
from typing import NamedTuple
from .typed_tuple import TypedTuple


# class GeocodedLocation(TypedTuple):
#     ne_lat = float
#     ne_lon = float
#     sw_lat = float
#     sw_lon = float
#     lat = float
#     lon = float
#     original_address = str
class GeocodedLocation(NamedTuple):
    ne_lat: float
    ne_lon: float
    sw_lat: float
    sw_lon: float
    lat: float
    lon: float
    original_address: str


# class ImageShape(TypedTuple):
#     w = int
#     h = int
#
#     def _parse_w(value):
#         if value <= 0:
#             raise ValueError(
#                     "Argument: w (width) must be greater than 0.")
#
#     def _parse_h(value):
#         if value <= 0:
#             raise ValueError(
#                     "Argument: h (height) must be greater than 0.")
class ImageShape(NamedTuple):
    w: int
    h: int


# class StaticMapType(TypedTuple):
#     value = str
#
#     def _parse_value(value):
#         if value not in ["satellite", "hybrid", "roadmap", "terrian"]:
#             raise ValueError("Invalid map type. Please choose one of " +
#                              "[\"satellite\", \"hybrid\", " +
#                              "\"roadmap\", \"terrain\"]")
class StaticMapType(NamedTuple):
    value: str


# class ImageFormat(TypedTuple):
#     value = str
#
#     def _parse_value(value):
#         if value not in \
#                 ["png", "png8", "png32", "gif", "jpg", "jpg-baseline"]:
#             raise ValueError(
#                     f"Invalid image format. Please choose one of " +
#                     "[\"png\", \"png8\", \"png32\", \"gif\", \"jpg\", " +
#                     "\"jpg-baseline\"]")
class ImageFormat(NamedTuple):
    value: str


__all__ = "GeocodedLocation", "ImageShape", "StaticMapType", "ImageShape"
