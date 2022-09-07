from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

other_headers = ['Statements','Season Zero','Season One','Season Two','Um, Actually YouTube Channel Episodes']
list_url = "https://um-actually.fandom.com/wiki/Um_Actually_Statements_(Questions)"
soupreq = bs(requests.get(list_url).content, "html.parser")

def drop_nl_arr(arr):
	return [x for x in arr if x != '\n']

# def drop_nl_string(in_str):
# 	return ""

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

all_headers = [x.contents[0] for x in top_div.find_all("span", class_="mw-headline")]
episode_titles = [x for x in all_headers if x not in other_headers]
#                                                                         list of q's from episode
master_list = [[[merge_str_list(question_row.contents) for question_row in drop_nl_arr(questions_table.contents)] for questions_table in drop_nl_arr(episode_table.contents[1].contents)] for episode_table in top_div.find_all("table")]

# Add titles and format to dict





# all_episode_tables = top_div.find_all("table")
# for episode_table in all_episode_tables:
# 	questions_list = [[merge_str_list(question_row.contents) for question_row in drop_nl_arr(questions_table.contents)] for questions_table in drop_nl_arr(episode_table.contents[1].contents)]
# 	questions = 0
