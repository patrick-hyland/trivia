import requests
from datetime import date
from bs4 import BeautifulSoup
import re

url = 'http://games.startribune.com/variety/comicgames/games/superquiz'
today = str(date.today())[5:]

resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')

quiz = soup.find_all('p')

clean_quiz = []
for line in quiz:
    clean_quiz.append(re.sub('<p>', "", str(line)).replace("</p>", "").replace("\"", " "))
trim_quiz = [line for line in clean_quiz if ("Answer_" not in line and "<hr/>" not in line)]

sep_index = [i for i, sent in enumerate(trim_quiz) if "ANSWERS" in sent][0]

questions = trim_quiz[:sep_index]
answers = trim_quiz[sep_index:]

with open("Desktop/super_quiz/{}_questions.txt".format(today), "w") as result:
    for i in questions:
        result.write("\n" + i)
with open("Desktop/super_quiz/{}_answers.txt".format(today), "w") as result:
    for i in answers:
        result.write("\n" + i)
