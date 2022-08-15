from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

list_url = "https://animevoiceover.fandom.com/wiki/Attack_on_Titan"
soupreq = bs(requests.get(list_url).content, "html.parser")

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

table = soupreq.find("div", class_="mw-parser-output")
lists = table.find_all("ul")

# scores = []
# header = ['Title', 'Score', 'Users'] #table[0]
# scores.append(header)
# for i in range(2,len(table),2):
# 	tr = table[i]
# 	li_url = tr.contents[3].contents[1].attrs.get("href")
# 	title = tr.contents[3].contents[3].contents[2].contents[0].contents[0].contents[0]
# 	li_soup = bs(requests.get(li_url).content, "html.parser")
# 	score_obj = li_soup.find("div", class_="fl-l score")
# 	users = score_obj.attrs.get("data-user")[:-6]
# 	score = score_obj.contents[0].contents[0]
# 	scores.append([title, score, users])

# df = pd.DataFrame(scores)
print()