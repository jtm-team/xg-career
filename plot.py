from data_scrapping import scrap_xg
import numpy as np
import pandas as pd
import math
import matplotlib.image as image
from matplotlib import artist
import matplotlib.patches as mpatches
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams
from matplotlib.patches import Arc
rcParams['font.family'] = 'DejaVu Sans'
rcParams['font.sans-serif'] = ['Franklin Gothic Medium', 'Franklin Gothic Book']

def plot_xg(index = 3423):

    player_name, df = scrap_xg(index)

    reversed_saisons = list(df.index)
    saisons = reversed_saisons[::-1]

    reversed_xg = list((df['goals-xg']))
    xg = reversed_xg[::-1]

    reversed_club = list((df['team']))
    club = reversed_club[::-1]

    transfered_from, transfered_to = {}, {}
    transfer = []
    actual = club[0]
    for i in range(1, len(club)):
        if club[i] != actual:
            transfered_from[saisons[i]] = actual
            transfered_to[saisons[i]] = club[i]
            actual = club[i]
            transfer.append(saisons[i])


    fig, ax = plt.subplots(figsize=(10, 10))
    matplotlib.style.use('fivethirtyeight')
    #ax.grid(False, color='xkcd:dark grey')
    ax.grid(visible=None, color='black')
    fig.patch.set_facecolor('#0b0d0f')
    ax.set_facecolor('#171b1e')



    # Adding graph and axes titles
    ax.set_ylabel('\nG - xG\n', color='xkcd:black', size=15)
    ax.set_xlabel('\nSeason', color='xkcd:black', size=15)
    ax.set_title(player_name + "'s performances", color='xkcd:black', size=25)

    ax.axhline(y=0, color='yellow', linestyle='--', linewidth=2, zorder=0.2)

    # Adding plot points from each of the three DataFrames in different colours
    ax.plot(saisons, xg)
    #for i in range(0,len(transfer)):
        #print(transfered_from)
        #ax.axvline(x=transfer[i], color='green', linestyle='-', linewidth=5, zorder=0.2)
        #plt.text(int(transfer[i]), xg[i], "TRANSFER", color="red", zorder=3,
        #        alpha=0.2, fontsize=260, fontweight='bold')
        #ax.text(i, i, transfered_from[transfer[i]], color="green", zorder=3,
        #        alpha=0.2, fontsize=26, fontweight='bold')
        #ax.text(i+2, i, transfered_to[transfer[i]], color="green", zorder=3,
        #        alpha=0.2, fontsize=26, fontweight='bold')




    plt.show()

    return fig

plot_xg()