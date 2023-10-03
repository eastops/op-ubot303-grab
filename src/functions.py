import requests
import os
import logging
from urllib.parse import urlparse
import watermark_remover_cli

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