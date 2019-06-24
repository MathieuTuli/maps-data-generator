"""Google Maps Portion"""

from typing import Optional
from argparse import ArgumentParser

import importlib.resources
import traceback
import logging

import googlemaps

from .components import GeocodedLocation, ImageShape

API_KEY = importlib.resources.read_text('mapsdg', '.api_key')


class GoogleMapsAPI:
    def __init__(self,
                 key: str = "",) -> None:
        if key:
            self.client = googlemaps.Client(key=key)
            self.key = key
        else:
            raise ValueError(f"Google Maps API Key -{key}- is not valid")

    def geocode_address(self,
                        addr: str) -> Optional[GeocodedLocation]:
        try:
            geocode_result = self.client.geocode(addr)
            logging.debug(
                    f"Geocoded result from -{addr}- \n\n{geocode_result}")
            for elem in geocode_result:
                keys = elem.keys()
                logging.debug(
                        f"\n\nKeys are {keys}")
                if "geometry" in keys:
                    values = elem["geometry"]
                    return GeocodedLocation(
                        ne_lat=values["bounds"]["northeast"]["lat"],
                        ne_lon=values["bounds"]["northeast"]["lng"],
                        sw_lat=values["bounds"]["southwest"]["lat"],
                        sw_lon=values["bounds"]["northeast"]["lng"],
                        lat=values["location"]["lat"],
                        lon=values["location"]["lng"],
                        original_address=addr,)
        except Exception:
            logging.debug(
                    f"Geocoded result for -{addr}- failed due to \n\n " +
                    f"{traceback.print_exc()}")
            return None

    def get_satellite_image(self,
                            geocoded_addr: GeocodedLocation,
                            image_zoom: int = 20,
                            image_shape: ImageShape = ImageShape(
                                w=640, h=400)) -> bool:
        image_request = f"https://maps.googleapis.com/maps/api/staticmap?" + \
            f"center={geocoded_addr.lat}%2C{geocode_result.lon}&" + \
            f"zoom={image_zoom}&size={image_shape.w}x{image_shape.h}&" + \
            "maptype=satellite&style=feature%3Aall%7Celement%3Alabels%7C" + \
            f"visibility%3Aoff&key={self.key}"
        logging.debug(f"Image request for -{geocoded_addr.original_address}-" +
                      f" is \n\n {image_request}")


parser = ArgumentParser(description=__doc__)
parser.add_argument('--log-level', default='INFO',
                    type=str)
args = parser.parse_args()
if args.log_level == 'INFO':
    logging.root.setLevel(logging.INFO)
elif args.log_level == 'DEBUG':
    logging.root.setLevel(logging.DEBUG)


if __name__ == "__main__":
    g = GoogleMapsAPI(key=API_KEY)
    geocode_result = g.geocode_address("233 Soper Place, Ottawa, Canada")
    g.get_satellite_image(geocode_result)
