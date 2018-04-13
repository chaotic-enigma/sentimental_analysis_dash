import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/column/restaurant-review'
response = requests.get(url)
html = response.content
#print(html)

soup = BeautifulSoup(html, 'html5lib')
#print(soup.prettify())

review = soup.findAll('p', attrs={'class' : 'summary'})
#print(review.prettify())
#print(len(review))

with open('restaurant-review.txt','w') as khana:
	for each_res in review:
		khana.write(each_res.text)
		khana.write('\n')
