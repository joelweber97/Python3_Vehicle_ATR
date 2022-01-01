import wget
import requests
from bs4 import BeautifulSoup

'''2018_imagery_site = 'https://data.tnris.org/f1d66250-4021-47df-9fe9-9fca286b0f50/resources/'
zip_file_structure = 'naip18-nc-cir-60cm_2697531_nc-cir.zip'


2020_imagery_site = 'https://data.tnris.org/aa5183ca-a1bd-4b5f-9b63-4ba48d01b83d/resources'
or 'https://data.tnris.org/collection?c=aa5183ca-a1bd-4b5f-9b63-4ba48d01b83d'
zip_file_structure = 'naip20-60cm_3102431_nc-cir.zip'

#need to get the url of each of the zip files with imagery.
#url='https://golang.org/dl/go1.1'https://data.tnris.org/collection?c=aa5183ca-a1bd-4b5f-9b63-4ba48d01b83d7.3.windows-amd64.zip'
paths.append(url)

'''



url = 'https://data.tnris.org/collection?c=aa5183ca-a1bd-4b5f-9b63-4ba48d01b83d#4.67/31.41/-100.12'
r = requests.get(url)

print(r)