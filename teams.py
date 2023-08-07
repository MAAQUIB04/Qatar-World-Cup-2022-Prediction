import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("C:/1043 project/international_matches.csv", parse_dates=['date'])
df.tail()
df.columns
df.isnull().sum()

# Top 10 Attacking Teams
fifa_offense = df[['date', 'home_team', 'away_team', 'home_team_mean_offense_score', 'away_team_mean_offense_score']]
home = fifa_offense[['date', 'home_team', 'home_team_mean_offense_score']].rename(columns={"home_team":"team", "home_team_mean_offense_score":"offense_score"})
away = fifa_offense[['date', 'away_team', 'away_team_mean_offense_score']].rename(columns={"away_team":"team", "away_team_mean_offense_score":"offense_score"})
fifa_offense = pd.concat([home, away])
fifa_offense = fifa_offense.sort_values(['date', 'team'],ascending=[False, True])
last_offense = fifa_offense
fifa_offense_top10 = fifa_offense.groupby('team').first().sort_values('offense_score', ascending=False)[0:10].reset_index()
fifa_offense_top10
print(fifa_offense_top10)

# plot
sns.barplot(data=fifa_offense_top10, x='offense_score', y='team', color="maroon")
plt.xlabel('Offense Score', size = 20)
plt.ylabel('Team', size = 20)
plt.title("Top 10 Attacking teams");
plt.show()

# Top 10 Midfield Teams
fifa_midfield = df[['date', 'home_team', 'away_team', 'home_team_mean_midfield_score', 'away_team_mean_midfield_score']]
home = fifa_midfield[['date', 'home_team', 'home_team_mean_midfield_score']].rename(columns={"home_team":"team", "home_team_mean_midfield_score":"midfield_score"})
away = fifa_midfield[['date', 'away_team', 'away_team_mean_midfield_score']].rename(columns={"away_team":"team", "away_team_mean_midfield_score":"midfield_score"})
fifa_midfield = pd.concat([home,away])
fifa_midfield = fifa_midfield.sort_values(['date','team'],ascending=[False,True])
last_midfield = fifa_midfield
fifa_midfield_top10 = fifa_midfield.groupby('team').first().sort_values('midfield_score',ascending=False)[0:10].reset_index()
print(fifa_midfield_top10)

# plot
sns.barplot(data=fifa_midfield_top10, x='midfield_score', y='team', color="blue")
plt.xlabel('Midfield Score', size = 20)
plt.ylabel('Team', size = 20)
plt.title("Top 10 Midfield teams");
plt.show()

# Top 10 Defensive Teams
fifa_defense = df[['date', 'home_team', 'away_team', 'home_team_mean_defense_score', 'away_team_mean_defense_score']]
home = fifa_defense[['date', 'home_team', 'home_team_mean_defense_score']].rename(columns={"home_team":"team", "home_team_mean_defense_score":"defense_score"})
away = fifa_defense[['date', 'away_team', 'away_team_mean_defense_score']].rename(columns={"away_team":"team", "away_team_mean_defense_score":"defense_score"})
fifa_defense = pd.concat([home, away])
fifa_defense = fifa_defense.sort_values(['date', 'team'],ascending=[False, True])
last_defense = fifa_defense
fifa_defense_top10 = fifa_defense.groupby('team').first().sort_values('defense_score', ascending = False)[0:10].reset_index()
print(fifa_defense_top10)

# plot
sns.barplot(data = fifa_defense_top10, x='defense_score', y='team', color="teal")
plt.xlabel('Defense Score', size = 20)
plt.ylabel('Team', size = 20)
plt.title("Top 10 Defense Teams")
plt.show()


