from bs4 import BeautifulSoup as bs
import requests, json
import pandas as pd

other_headers = ['Statements','Season Zero','Season One','Season Two','Um, Actually YouTube Channel Episodes']
list_url = "https://um-actually.fandom.com/wiki/Um_Actually_Statements_(Questions)"
soupreq = bs(requests.get(list_url).content, "html.parser")

def drop_nl_arr(arr):
	return [x for x in arr if x != '\n']

def f_header(s: str):
	a: str = ""
	if s.startswith("Ep"):
		if s[2] == ',':
			s = s[:2] + '.' + s[3:]
	if s.count(':') == 0:
		comma_loc = s.find(',')
		if comma_loc in [5,6]:
			s = s[:comma_loc] + ':' + s[comma_loc + 1:]
	return s

def merge_str_list(arr):
	if str(type(arr)) == "<class 'str'>":
		return arr.strip()
	if len(arr) == 1:
		return arr[0].strip()
	result = ""
	for element in arr:
		if element == '\n':
			continue
		if str(type(element)) != "<class 'bs4.element.Tag'>": # if element is a string
			result += (element.strip() + " ")
		else:
			result += (element.text.strip() + " ")
	return result

top_div = soupreq.find("div", class_="mw-parser-output")

all_headers = [str(x.contents[0]) for x in top_div.find_all("span", class_="mw-headline")]
all_headers[22] = all_headers[22][:3] + all_headers[22][4:]
episode_titles = [f_header(x) for x in all_headers if x not in other_headers]

master_list = [[[merge_str_list(question_row.contents) for question_row in drop_nl_arr(questions_table.contents)] for questions_table in drop_nl_arr(episode_table.contents[1].contents)] for episode_table in top_div.find_all("table")]

# format to dict
master_dict = {}
for episode in master_list:

	if ['Statement', 'Answer', 'Corrected'] in episode:
		episode.remove(['Statement', 'Answer', 'Corrected'])
	if ['Statement', 'Answer', 'Corrected?'] in episode:
		episode.remove(['Statement', 'Answer', 'Corrected?'])

	for idx, question in enumerate(episode):
		episode[idx] = {'Statement': question[0], 'Answer': question[1], 'Corrected': question[2]}

# add titles
for idx, episode_title in enumerate(episode_titles):
	master_dict[episode_title[:episode_title.find(':')]] = {"episode_title": episode_title,"question_list": master_list[idx]}

# TODO overrides other episodes.

print()

# all_episode_tables = top_div.find_all("table")
# for episode_table in all_episode_tables:
# 	questions_list = [[merge_str_list(question_row.contents) for question_row in drop_nl_arr(questions_table.contents)] for questions_table in drop_nl_arr(episode_table.contents[1].contents)]
# 	questions = 0
