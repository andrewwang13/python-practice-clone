import csv
import requests
import re
from BeautifulSoup import BeautifulSoup

base_url='https://www.census.gov'
main_url='https://www.census.gov/eos/www/naics/reference_files_tools/1997/1997.html'
response=requests.get(main_url)
html=response.content
soup=BeautifulSoup(html)

all_data=[]
# Pull out sector URLs, make list
url_list=[]
table=soup.find('table',summary='The following table provides links to 1997 NAICS industry titles and descriptions.  Downloadable files are listed at the bottom of the page.')

for i in table.findAll('a'):
	url_Path=i['href']
	url_list.append(base_url+url_Path)

# print url_list

for i in table.findAll('a'):
	row=[]
	row.append(i.text)
	row.append(i['title'])
	all_data.append(row)

def getSector(url):
	headings_list=[]
	sector_response=requests.get(url)
	sector_html=sector_response.content
	sector_soup=BeautifulSoup(sector_html)

	headings=sector_soup.findAll('h3')[4:]
	row=[]
	for i in headings:
		
		i_text=i.text
		row.append(i_text.split(" ",1))
	return row
	
for j in url_list:
	all_data=all_data+(getSector(j))

# print all_data

file = open("./1997_naics.csv","wb")
writer = csv.writer(file)
writer.writerows(all_data)
