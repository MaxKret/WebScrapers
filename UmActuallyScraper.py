from bs4 import BeautifulSoup as bs
import requests

other_headers = ['Statements','Season Zero','Season One','Season Two','Um, Actually YouTube Channel Episodes']
list_url = "https://um-actually.fandom.com/wiki/Um_Actually_Statements_(Questions)"
soupreq = bs(requests.get(list_url).content, "html.parser")

def drop_nl(arr):
	return [x for x in arr if x != '\n']

def merge_str_list(arr):
	if len(arr) == 1:
		return arr[0]
	result = ""
	for element in arr:
		if str(type(element)) != "<class 'bs4.element.Tag'>": # if element is a string
			result += element
		else:
			result += element.text
	return result

top_div = soupreq.find("div", class_="mw-parser-output")

all_headers = [x.contents[0] for x in top_div.find_all("span", class_="mw-headline")]
episode_titles = [x for x in all_headers if x not in other_headers]
#                                                                         list of q's from episode
master_list = [[[question_row.contents for question_row in drop_nl(questions_table.contents)] for questions_table in drop_nl(episode_table.contents[1].contents)] for episode_table in top_div.find_all("table")]

for x in master_list:
	for y in x:
		for z in y:
			out = merge_str_list(z)


all_episode_tables = top_div.find_all("table")
for episode_table in all_episode_tables:
	questions_list = [[question_row.contents for question_row in drop_nl(questions_table.contents)] for questions_table in drop_nl(episode_table.contents[1].contents)]
	questions = 0
