import requests
import os
import logging
import cv2
from urllib.parse import urlparse
import watermark_remover_cli
import urllib.parse
from PIL import Image

def remove_watermark(input_image_path, output_image_path):
    image = Image.open(input_image_path)
    # define the region of the watermark
    coords = "2046,988,1225,982"
    coords_list = coords.split(",")
    coords_int = [int(coord) for coord in coords_list]
    watermark_region = tuple(coords_int)
    # create a new image without the watermark
    image_without_watermark = image.crop(watermark_region)
    # save the new image
    image_without_watermark.save(output_image_path)

def detect_edges(image_path):
    # read the image
    image = cv2.imread(image_path)
    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    # detect edges using the Canny algorithm
    edges = cv2.Canny(blurred, 50, 150)
    # return the edges
    return edges

# function to download the file based on the specified URL
def download_file(url, file_path):
    chunk_size = 1024 * 1024  # 1 MB
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    return os.path.exists(file_path)


# function to convert the URL provided into image original URL and extract the non watermarked image
def convert_url(url):
    # Parse the URL to extract query parameters
    parsed_url = urllib.parse.urlparse(url)

    # Construct the new URL by replacing the scheme and netloc (domain) with the parsed URL's netloc
    new_url = urllib.parse.urlunparse(("", parsed_url.netloc, parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment))
    return new_url

# watermark removal function
def remove_watermark(input_image_file_path, output_image_file_path):
    # Create an instance of the watermark remover tool
    watermark_remover = watermark_remover_cli.WatermarkRemover()
    # Set the input image file path
    watermark_remover.set_input_image_file_path(input_image_file_path)
    # Set the output image file path
    watermark_remover.set_output_image_file_path(output_image_file_path)
    # Remove the watermark
    watermark_remover.remove_watermark()
    # Save the output image file
    watermark_remover.save_output_image_file()