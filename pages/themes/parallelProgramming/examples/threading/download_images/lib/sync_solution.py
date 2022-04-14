import re
import requests
from typing import List

def download_image(url:str)->None:
	print(f'Downloading {url}')
	response = requests.get(url)
	if response.ok:
		return response.content

def write_to_file(filename:str, bytes:bytes):
	with open(filename, 'wb') as fh:
		fh.write(bytes)

def make_filename(url:str)->str:
	rx = re.compile(r'\/([\w-]+)\.jpg$')
	match = rx.search(url)
	if match:
		return match.group(1) + '.jpg'

def download_all(urls:List[str], output_dir:str)->None:
	for url in urls:
		img_bytes = download_image(url)
		filename = make_filename(url)
		write_to_file(output_dir + filename, img_bytes)

