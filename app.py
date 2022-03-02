import streamlit as st
from utils.plot import plot_xg
from utils.name_id_scrapping import name_id_scrapping

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



