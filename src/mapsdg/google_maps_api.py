"""Google Maps Portion"""

from argparse import ArgumentParser
from pathlib import Path
from typing import Optional, Tuple, List, Union

import importlib.resources
import traceback
import logging
import requests

from PIL import Image
import googlemaps

from .components import GeocodedLocation, ImageShape, StaticMapType, \
    ImageFormat

API_KEY = importlib.resources.read_text('mapsdg', '.api_key')


class GoogleMapsAPI:
    def __init__(self,
                 key: str = "",) -> None:
        if key:
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
                    f"Geocoded result for - {addr} - failed due to \n\n " +
                    f"{traceback.print_exc()}")
            return None

    def get_static_image_url(self,
                             addr: Union[str, GeocodedLocation],
                             map_type: str = "satellite",
                             image_zoom: int = 20,
                             image_shape: ImageShape = ImageShape(
                                  w=640, h=400),
                             image_format: str = "png") -> Optional[str]:
        logging.debug(f"Arguments: \n" +
                      f"  addr:{addr}\n  map_type:{map_type}\n" +
                      f"  image_zoom:{image_zoom}\n" +
                      f"  image_shape:{image_shape}\n" +
                      f"  image_format:{image_format}")
        if isinstance(addr, GeocodedLocation):
            center = f"{addr.lat},{addr.lon}&"
        elif isinstance(addr, str):
            center = addr
        else:
            logging.error(f"Argument:addr - {addr} - is not of type:str" +
                          " or GeocodedLocation")
            raise ValueError(f"Argument:addr - {addr} - is not of type:str" +
                             "or GeocodedLocation")
        image_format = ImageFormat(image_format)
        map_type = StaticMapType(map_type)
        image_request_url = (
                "https://maps.googleapis.com/maps/api/staticmap?" +
                f"center={center}&" +
                f"zoom={image_zoom}&" +
                f"size={image_shape.w}x{image_shape.h}&" +
                f"maptype={map_type.value}&" +
                f"format={image_format.value}&" +
                "style=feature%3Aall%7Celement%3Alabels%7Cvisibility%3Aoff&" +
                f"key={self.key}".strip())
        logging.debug(f"Image request for - {addr} -" +
                      f" is \n{image_request_url}")
        return image_request_url

    def download_static_images(
            self,
            addr: Optional[Union[str, GeocodedLocation]] = None,
            file_name: Optional[Union[str, Path]] = None,
            from_file: bool = False,
            directory: str = 'static-images') -> Tuple[List[str], bool]:
        if from_file:
            if not Path(file_name).is_file():
                raise ValueError(f"File - {file_name} - does not exist")
            with open(file_name, 'r') as f:
                lines = f.readlines()
        else:
            lines = [addr]
        for line in lines:
            try:
                url = self.get_static_image_url(addr=line)
                try:
                    self.download_image_from_url(url=url,
                                                 directory=directory,
                                                 file_name=line)
                except Exception:
                    logging.error(f"Could not get url for addr - {addr} - " +
                                  f"due to\n\n{traceback.print_exc()}")
                    return (addr, False)

            except Exception:
                logging.error(f"Could not get url for addr - {addr} - due to" +
                              f"\n\n{traceback.print_exc()}")
                return (addr, False)
        return ((), True)

    def download_image_from_url(
            self,
            url: str,
            directory: str = 'static-images',
            file_name: Optional[str] = None) -> bool:
        if not Path(directory).is_dir():
            Path(directory).mkdir(parents=True)
        extension = url.split('format=')[1].split('&')[0]
        if not file_name:
            file_name = url.split(
                    "https://maps.googleapis.com/maps/api/staticmap?"
                    )[1].split('key=')[0]
        try:
            response = requests.get(url, stream=True).raw
            img = Image.open(response)
            img.save(f'{directory}/{file_name}.{extension}')
            logging.debug(f"Retrieving image from {url} succeeded")
            return True
        except Exception:
            logging.debug(f"Retrieving image from {url} failed due to \n\n" +
                          f"{traceback.print_exc()}")
            return False


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
    # geocode_result = g.geocode_address("233 Soper Place, Ottawa, Canada")
    g.download_static_images(file_name='addresses.txt', from_file=True)