import json
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
from data_scrapping import scrap_xg

player_name_id = {}

for i in range(5000,10000):
    print(i)
    try:
        player_name, df = scrap_xg(i)
        player_name_id[i] = player_name
    except:
        pass
print(player_name_id)