
import requests as r
from bs4 import BeautifulSoup as soup
import pandas as pd

url = 'http://www.enchantedlearning.com/history/us/pres/list.shtml'

page_data = r.get(url)

page_soup = soup(page_data.text, 'html.parser')

page_data = page_soup.find_all('table')[8]

prez_df = pd.DataFrame()

for prez in range(1, 45 + 1):
    table_data = page_data.find_all('tr')[prez]
    prez_name = table_data.find_all('td')[0].text
    prez_party = table_data.find_all('td')[1].text
    prez_years = table_data.find_all('td')[2].text
    vice_prez = table_data.find_all('td')[3].text
    prez_df = prez_df.append(pd.DataFrame({'name': prez_name, 'party': prez_party, 'term': prez_years, 'vice_president': vice_prez},index=[0]),ignore_index = True)

prez_df.to_csv('list_of_us_presidents.csv')
