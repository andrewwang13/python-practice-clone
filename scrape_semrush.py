import csv
import requests
from BeautifulSoup import BeautifulSoup
import time

with open('./llc_queries.csv', 'rb') as f:
    reader = csv.reader(f)
    query_list = list(reader)

# print query_list

search_terms=[]

for i in range(len(query_list))[1:]:
	term=query_list[i][0].replace(' ','%20')
	search_terms.append(term)

# print search_terms

base_url='https://www.semrush.com/info/'

full_url_list=[]
for j in search_terms:
	full_url=base_url+j+'+(keyword)'
	full_url_list.append(full_url)

# print full_url_list

# def getData(url):
url='https://www.semrush.com/info/llc%20pros%20and%20cons+(keyword)'
response=requests.get(url)
html=response.content
soup=BeautifulSoup(html)

data=[]

# print soup
for i in soup.findAll('td'):
	print i
	# data.append(i)

	# return data

# print getData('https://www.semrush.com/info/llc%20pros%20and%20cons+(keyword)')
