# Parcel Postbox Locations

**Note: You can use [Services Near You](https://www.royalmail.com/services-near-you) and filter by Parcel postboxes, but I wasn't awake enough when I wrote this code to notice that.**

Since the main page for finding Royal Mail Parcel postboxes is [not particularly useful](https://www.royalmail.com/d8/parcel-post-boxes), this repo contains a script which uses that page to generate a static Google Maps map so they can be geolocated easier. 

Below is a screen capture of a portion of the map, and the streetview of one of the locations proving this solution works.

![postal locations](https://user-images.githubusercontent.com/3343469/145773932-1a85e3f6-2a3f-4427-93c2-672f21ec2926.PNG)
![postbox](https://user-images.githubusercontent.com/3343469/145773942-c560f13e-8626-4233-913a-88011251d5ba.PNG)

### Requirements 

- Python 3.X
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/) 
- [gmplot](https://github.com/gmplot/gmplot)
- Google Javascript Maps API Key

### Usage 

1. Put your API key in [line 8](https://github.com/stuart-bradley/parcel-postbox-locations/blob/main/all_parcelbox_locations.py#L8).
2. Run the script. 
3. Open `parcelbox_map.html`
