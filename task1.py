import requests
from pprint import pprint
from bs4 import BeautifulSoup
URL = "https://www.imdb.com/india/top-rated-indian-movies/"
sample  = requests.get(URL)
soup = BeautifulSoup(sample.text,"html.parser")
tBody = soup.find("tbody",class_="lister-list")
table_rows = tBody.find_all("tr")
def scrape_top_list(table_rows):
	movies_list = []
	for row in table_rows:
		dic = {}
		name = row.find("td", class_ = "titleColumn").a.get_text()
		position = row.find("td", class_ = "posterColumn").span["data-value"]
		year = row.find("td", class_= "titleColumn").span.get_text()
		url = row.find("td",class_="posterColumn").a["href"]
		movies_link = "https://www.imdb.com/" + url
		ratings = row.find("td",class_="ratingColumn imdbRating").strong.get_text()
		dic['position'] = position
		dic['name'] = name
		dic['year'] = year
		dic['ratings'] = ratings
		dic['url'] = movies_link
		movies_list.append(dic)
	return(movies_list)

movies = scrape_top_list(table_rows)
pprint(movies)
