from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

list_url = "https://myanimelist.net/topanime.php"
soup = bs(requests.get(list_url).content, "html.parser")
table = soup.find("table", class_="top-ranking-table").contents

scores = []
header = ['Title', 'Score', 'Users'] #table[0]
scores.append(header)
for i in range(2,len(table),2):
	tr = table[i]
	li_url = tr.contents[3].contents[1].attrs.get("href")
	title = tr.contents[3].contents[3].contents[2].contents[0].contents[0].contents[0]
	li_soup = bs(requests.get(li_url).content, "html.parser")
	score_obj = li_soup.find("div", class_="fl-l score")
	users = score_obj.attrs.get("data-user")[:-6]
	score = score_obj.contents[0].contents[0]
	scores.append([title, score, users])

df = pd.DataFrame(scores)
print()