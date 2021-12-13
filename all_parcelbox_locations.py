import gmplot
import re
import requests

from bs4 import BeautifulSoup

# API Requires Javascript Maps API and Unrestricted access if running locally. 
apikey = ''
# Map centered on London England.
gmap = gmplot.GoogleMapPlotter(51.487308, -0.110561, 14, apikey=apikey)
url = 'https://www.royalmail.com/d8/parcel-post-boxes'
# Royal mail doesn't allow the standard requests user-agent.
headers = {'User-Agent': 'Mozilla/5.0'}
# query=1.000,-0.123 
rgx = r'\&query\=(-?\d+\.\d+),(-?\d+.\d+)'
parcelbox_lats, parcelbox_lngs = [], []

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
href_tags = soup.find_all(href=True)

for tag in href_tags:
	result = re.search(
		r'\&query\=(-?\d+\.\d+),(-?\d+.\d+)', 
		tag.get('href', '')
	)
	if result:
		parcelbox_lats.append(float(result.group(1)))
		parcelbox_lngs.append(float(result.group(2)))

gmap.scatter(parcelbox_lats, parcelbox_lngs, c='red', size=40)
gmap.draw('parcelbox_map.html')