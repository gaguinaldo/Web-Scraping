#Standard Imports

import requests
from bs4 import BeautifulSoup as soup
import xlsxwriter

#Script to scrape the review text.

page_num = 0

while page_num <= 200:

	url = "https://www.yelp.com/biz/monkey-house-cafe-huntington-beach?start=%s" % page_num

	r = requests.get(url)

	page_soup = soup(r.content, "lxml")

	review_container = page_soup.findAll("div", {"class": "review-content"})

	#write to excel  

	workbook = xlsxwriter.Workbook('output.xlsx')

	worksheet = workbook.add_worksheet()

	#header

	worksheet.write('A1','header')

	#writing each review
	
	row = 1
	
	for review in review_container:
	    string = str(review.p.text)
	    worksheet.write(row, 0, string)
	    row += 1
	
	page_num += 20

workbook.close()