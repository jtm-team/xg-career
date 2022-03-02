import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import requests
from bs4 import BeautifulSoup
from plot import plot_xg
from name_id_scrapping import name_id_scrapping

dict_id_name = name_id_scrapping()
reversed_dict_id_name = dict((v, k) for k, v in dict_id_name.items())


st.title('Player lethality across the years')

st.markdown("""
This app performs simple webscraping of Football player stats data (focusing on Goal - Expected Goals)!
* **Data source:** [understat.com](https://understat.com/) \n \n.
""")

st.sidebar.header('Data Selection')
selected_name = st.sidebar.selectbox('Player Name', list(dict_id_name.values()))

fig = plot_xg(reversed_dict_id_name[selected_name])

st.pyplot(fig)



