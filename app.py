# app.py

import sys
import logging
import os
import json
import requests
from urllib.parse import urlparse

logging.basicConfig(level=logging.INFO)

sys.path.append("/src")

# download the image based on specified link
from src.functions import download_file, convert_url


if __name__ == "__main__":
    # Get the absolute path of the downloads directory.
    downloads_dir = os.path.abspath("downloads")
    # Create the downloads directory if it doesn't exist.
    os.makedirs(downloads_dir, exist_ok=True)
    # Get the URL from the command line arguments.
    url = "https://media.gettyimages.com/id/696311622/photo/caucasian-bearded-viking-man-in-the-dunes-at-daytime.jpg?s=2048x2048&w=gi&k=20&c=sDMXntQ-Wx9OyQnu0kP13k9fvvjnRGohXOM4HTHfXcM="
    # Download the file.
    success = download_file(url, os.path.join(downloads_dir, os.path.basename(urlparse(url).path)))
    if success:
        logging.info(f"File downloaded successfully: {downloads_dir}")
    else:
        logging.error(f"Failed to download file: {url}")
    
    
