# from argparse import ArgumentParser
from typing import Optional

import traceback
import logging

from skimage import io
import numpy as np


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

__all__ = "download_image_from_url"
