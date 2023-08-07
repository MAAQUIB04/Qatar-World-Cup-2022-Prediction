import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

FIFA22 = pd.read_csv("C:/1043 project/players_22.csv")
FIFA22.shape

# Selecting player data for Top 20 player analysis
interesting_columns = ['short_name', 'age', 'nationality_name', 'overall', 'potential', 'club_name', 'value_eur', 'wage_eur', 'player_positions']
FIFA22 = pd.DataFrame(FIFA22, columns=interesting_columns)
FIFA22.info()
FIFA22.head(5)
print(FIFA22.head(5))

# Selecting the teams that are participating in the world cup this year
list_2022 = ['Qatar', 'Germany', 'Denmark', 'Brazil', 'France', 'Belgium', 'Croatia', 'Spain', 'Serbia', 'England', 'Switzerland', 'Netherlands', 'Argentina', 'IR Iran', 'Korea Republic', 'Japan', 'Saudi Arabia', 'Ecuador', 'Uruguay', 'Canada', 'Ghana', 'Senegal', 'Portugal', 'Poland', 'Tunisia', 'Morocco', 'Cameroon', 'USA', 'Mexico', 'Wales', 'Australia', 'Costa Rica']
FIFA22['Position'] = FIFA22['player_positions'].str.split(",").str[0]
FIFA22 = FIFA22[["short_name", "age", "nationality_name", 'overall', 'potential', "club_name", "Position", "value_eur", "wage_eur"]]
FIFA22 = FIFA22[(FIFA22["nationality_name"].apply(lambda x: x in list_2022))]
FIFA22['nationality_name'].unique()
FIFA22.head(5)
print(FIFA22.head(5))

# TOP 20 PLAYER (OVERALL)
Overall = FIFA22["overall"]
footballer_name = FIFA22["short_name"]

x = FIFA22['short_name'].head(20)
y = FIFA22['overall'].head(20)

# plot
ax= sns.barplot(x=y, y=x, color="orangered", orient='h')
plt.xlabel('Overall Ratings', size=20)
plt.ylabel('Player', size=20)
plt.title('Top 20 players QATAR World Cup')
plt.show()

# BEST SQUAD (4-3-3)
def get_best_squad(formation):
    FIFA22_copy = FIFA22.copy()
    store = []

    # iterate through all positions in the input formation and get players with highest overall respective to the position
    for i in formation:
        store.append([
            i,
            FIFA22_copy.loc[[FIFA22_copy[FIFA22_copy['Position'] == i]['overall'].idxmax()]]['short_name'].to_string(
                index=False),
            FIFA22_copy[FIFA22_copy['Position'] == i]['overall'].max(),
            FIFA22_copy.loc[[FIFA22_copy[FIFA22_copy['Position'] == i]['overall'].idxmax()]]['age'].to_string(
                index=False),
            FIFA22_copy.loc[[FIFA22_copy[FIFA22_copy['Position'] == i]['overall'].idxmax()]]['club_name'].to_string(
                index=False),
            FIFA22_copy.loc[[FIFA22_copy[FIFA22_copy['Position'] == i]['overall'].idxmax()]]['value_eur'].to_string(
                index=False),
            FIFA22_copy.loc[[FIFA22_copy[FIFA22_copy['Position'] == i]['overall'].idxmax()]]['wage_eur'].to_string(
                index=False)
        ])
        FIFA22_copy.drop(FIFA22_copy[FIFA22_copy['Position'] == i]['overall'].idxmax(),
                         inplace=True)
    # return store with only necessary columns
    return pd.DataFrame(np.array(store).reshape(11, 7),
                        columns=['Position', 'short_name', 'overall', 'age', 'club_name', 'value_eur',
                                 'wage_eur']).to_string(index=False)

squad_433 = ['GK', 'RB', 'CB', 'CB', 'LB', 'CDM', 'CM', 'CAM', 'RW', 'ST', 'LW']
print ('4-3-3')
print (get_best_squad(squad_433))











