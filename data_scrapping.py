import json
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
from random import randint

def scrap_xg(index = 3423):
    base_url = 'https://understat.com/player/'
    #index = randint(1,5000)

    url = base_url + str(index)
    page_connect = urlopen(url)
    page_html = BeautifulSoup(page_connect, "html.parser")
    page_html.findAll(name="script")
    json_raw_string = page_html.findAll(name="script")[1].string
    start_ind = json_raw_string.index("\\")
    stop_ind = json_raw_string.index("')")

    find_name = page_html.findAll(id="header")
    player_name = find_name[0].text.strip()

    data = json_raw_string[start_ind:stop_ind]
    data = data.encode("utf8").decode("unicode_escape")

    data = json.loads(data)

    season, goals, xg, diff_goal_xg, team = [], [], [], [], []

    df = pd.DataFrame(columns=["Season", "Goals-xG", "goals", "xG", "Team"], index=range(0, len(data['season'])))
    for i in range(len(data['season'])):
        season.append(data['season'][i]["season"])
        goals.append(data['season'][i]["goals"])
        xg.append(data['season'][i]["xG"])
        diff_goal_xg.append(float(data['season'][i]["goals"]) - float(data['season'][i]["xG"]))
        team.append(data['season'][i]["team"])
        #print(data['season'][i])
    df = pd.DataFrame(data=zip(goals,xg,diff_goal_xg, team),columns=['goals','xG','goals-xg', "team"], index=season)

    return player_name, df

player_name, df = scrap_xg(index = 3423)


