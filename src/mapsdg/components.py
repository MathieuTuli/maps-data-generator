'''Components for typing purposes'''
# from dataclasses import dataclass
from typing import TypeVar, NamedTuple, NewType, List, Union, Any


class GeocodedLocation(NamedTuple):
    ne_lat: float
    ne_lon: float
    sw_lat: float
    sw_lon: float
    lat: float
    lon: float
    original_address: str
