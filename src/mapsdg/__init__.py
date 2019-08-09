# from argparse import ArgumentParser
from pathlib import Path
from typing import Union, Optional, List, Tuple

import traceback
import requests
import logging

from PIL import Image
from skimage import io
import numpy as np
import cv2

from .google_maps_api import GoogleMapsAPI
from .components import GeocodedLocation


def download_static_images(
        google_maps_api: GoogleMapsAPI,
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
            url = google_maps_api.get_static_image_url(addr=line)
            try:
                download_image_from_url(url=url,
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


def get_image_from_url(
        url: str,) -> Optional[np.ndarray]:
    print(url)
    try:
        img = io.imread(url)
        logging.debug(f"Retrieving image from {url} succeeded")
        return img
    except Exception:
        logging.debug(f"Retrieving image from {url} failed due to \n\n" +
                      f"{traceback.print_exc()}")
        return None


# parser = ArgumentParser(description=__doc__)
# parser.add_argument('--log-level', default='INFO',
#                     type=str)
# args = parser.parse_args()
# if args.log_level == 'INFO':
#     logging.root.setLevel(logging.INFO)
# elif args.log_level == 'DEBUG':
#     logging.root.setLevel(logging.DEBUG)

    # if not Path(directory).is_dir():
    #     Path(directory).mkdir(parents=True)
    # extension = url.split('format=')[1].split('&')[0]
    # if not file_name:
    #     file_name = url.split(
    #         "https://maps.googleapis.com/maps/api/staticmap?"
    #     )[1].split('key=')[0]

__all__ = "download_static_images", "download_image_from_url"
