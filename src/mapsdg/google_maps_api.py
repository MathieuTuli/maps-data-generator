"""Google Maps Portion"""

from argparse import ArgumentParser
# from pathlib import Path
from typing import Optional, Union

import importlib.resources
import traceback
import logging
# import requests
import re

# from PIL import Image
import googlemaps

from .components import GeocodedLocation, ImageShape, StaticMapType, \
    ImageFormat, LatLon, ViewType, Heading, FieldOfView, Pitch, Radius

API_KEY = importlib.resources.read_text('mapsdg', '.api_key')


class GoogleMapsAPI:
    def __init__(self,
                 key: str = "",) -> None:
        if isinstance(key, str):
            self.client = googlemaps.Client(key=key)
            self.key = key
        else:
            raise ValueError(f"Google Maps API Key - {key} - is not valid")

    def geocode_address(self,
                        addr: str) -> Optional[GeocodedLocation]:
        try:
            geocode_result = self.client.geocode(addr)
            logging.debug(
                f"Geocoded result from - {addr} - \n\n{geocode_result}")
            if not geocode_result:
                return None
            for elem in geocode_result:
                keys = elem.keys()
                logging.debug(
                    f"\n\nKeys are {keys}")
                if "geometry" in keys:
                    values = elem["geometry"]
                    if 'bounds' not in values:
                        return None
                    return GeocodedLocation(
                        ne_lat=values["bounds"]["northeast"]["lat"],
                        ne_lon=values["bounds"]["northeast"]["lng"],
                        sw_lat=values["bounds"]["southwest"]["lat"],
                        sw_lon=values["bounds"]["northeast"]["lng"],
                        lat=values["location"]["lat"],
                        lon=values["location"]["lng"],
                        original_address=addr,)
        except Exception as e:
            logging.debug(
                f"Geocoded result for - {addr} - failed due to \n\n " +
                f"{traceback.print_exc()}")
            raise e

    def get_static_center_string(
            self,
            addr: Union[LatLon, GeocodedLocation, str],) -> str:
        if isinstance(addr, str):
            addr = self.geocode_address(addr)

        if isinstance(addr, GeocodedLocation) or isinstance(addr, LatLon):
            return f"{addr.lat},{addr.lon}"
        else:
            err = (f"Argument:addr - {addr} - is not of type: str" +
                   " or GeocodedLocation or LatLon")
            logging.error(err)
            raise ValueError(err)

    def get_image_url(
            self,
            addr: Union[LatLon, GeocodedLocation, str],
            view_type: ViewType,
            map_type: StaticMapType = StaticMapType.satellite,
            image_zoom: int = 20,
            image_shape: ImageShape = ImageShape(width=640, height=400),
            image_format: ImageFormat = ImageFormat.png,
            heading: Heading = Heading(),
            fov: FieldOfView = FieldOfView(),
            pitch: Pitch = Pitch(),
            radius: Radius = Radius(),
            additional_parameters: str = "") -> Optional[str]:
        logging.debug(f"get_static_image_url Arguments: \n" +
                      f"  addr:{addr}\n  map_type:{map_type}\n" +
                      f"  image_zoom:{image_zoom}\n" +
                      f"  image_shape:{image_shape}\n" +
                      f"  image_format:{image_format}")
        result = re.match("^(.+=.+&)*$", additional_parameters)
        if not result:
            err = "Incorrect additioanl options. Must follow the" +\
                "regex: \"^(.+=.+&)*$\""
            logging.error(err)
            raise ValueError(err)
        center = self.get_static_center_string(addr)
        if view_type.name == 'staticmap':
            image_request_url = (
                f"https://maps.googleapis.com/maps/api/{view_type.name}?" +
                f"center={center}&" +
                f"zoom={image_zoom}&" +
                f"size={image_shape.width}x{image_shape.height}&" +
                f"maptype={map_type.name}&" +
                f"format={image_format.name}&" +
                "style=feature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff&" +
                f"key={self.key}".strip() +
                additional_parameters)
        elif view_type.name == 'streetview':
            image_request_url = (
                f"https://maps.googleapis.com/maps/api/{view_type.name}?" +
                f"location={center}&" +
                f"heading={heading.value}&" +
                f"size={image_shape.width}x{image_shape.height}&" +
                f"fov={fov.value}&" +
                f"pitch={pitch.value}&" +
                f"radius={radius.value}&" +
                f"format={image_format.name}&" +
                "style=feature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff&" +
                f"key={self.key}".strip() +
                additional_parameters)
        logging.debug(f"Image request for - {addr} -" +
                      f" is \n{image_request_url}")
        return image_request_url


# parser = ArgumentParser(description=__doc__)
# parser.add_argument('--log-level', default='INFO',
#                     type=str)
# args = parser.parse_args()
# if args.log_level == 'INFO':
#     logging.root.setLevel(logging.INFO)
# elif args.log_level == 'DEBUG':
#     logging.root.setLevel(logging.DEBUG)


# if __name__ == "__main__":
    # g = GoogleMapsAPI(key=API_KEY)
    # geocode_result = g.geocode_address("233 Soper Place, Ottawa, Canada")
    # g.download_static_images(file_name='addresses.txt', from_file=True)
