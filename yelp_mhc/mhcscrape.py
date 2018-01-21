#Script to scrape review text from a page on yelp.

#Standard Imports

import requests			
from bs4 import BeautifulSoup as soup

"""

Each page on yelp displays 10 reviews.  To advance to the next page, the url 
"?start=" string changes by 20.  Therefore, reviews 11-20 end with "?start=20", 
reviews 21-30 end with "?start=40" etc. 

The first page on yelp can be reached with the ending url "?start=0"  

"""

page_num = 0

url2 = "https://www.yelp.com/biz/monkey-house-cafe-huntington-beach?start=%s" % page_num

r = requests.get(url2)						#Download webpage
page_soup = soup(r.content, "lxml")			#Parse in webpage into BeautifulSoup

review_container = page_soup.findAll("div", {"class": "review-content"})	

for review in review_container:
    review_text = review.p.text  		
    print(review_text + '\n') 