# app.py

import sys
import logging
import os
import json
import requests
from urllib.parse import urlparse
from selenium import webdriver
from PIL import Image

logging.basicConfig(level=logging.INFO)
sys.path.append("/src")
# download the image based on specified link
from src.functions import download_file, remove_watermark

import cv2
import matplotlib.pyplot as plt

def remove_watermark(image):
  """Removes a watermark from an image.

  Args:
    image: The image with the watermark.

  Returns:
    The image without the watermark.
  """

  # Select the watermark area in the image.
  watermark_mask = cv2.selectROI("Image with watermark", image)

  # Inpaint the watermark area.
  inpainted_image = cv2.inpaint(image, watermark_mask, 3, cv2.INPAINT_NS)

  return inpainted_image

# Load the image with the watermark.
image = cv2.imread("image_with_watermark.jpg")

# Remove the watermark from the image.
inpainted_image = remove_watermark(image)

# Save the image without the watermark.
cv2.imwrite("image_without_watermark.jpg", inpainted_image)


if __name__ == "__main__":
    # Get the absolute path of the downloads directory.
    # Create the downloads directory if it doesn't exist.
    downloads_dir = os.path.abspath("downloads")

    os.makedirs(downloads_dir, exist_ok=True)
    # Get the URL from the command line arguments.

    extract_texture_features("downloads/viking-warrior-king-in-a-forest.jpg", "downloads/output2.png")
    