# -*- coding: utf-8 -*-
"""Fifa-world-cup.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_kOWW63zG0LNJ0If6na2Yda3vE71a-By
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

y=pd.read_csv('Fifa_world_cup_matches.csv')

y.head()

y.columns

y.corr

y.info()

y.notnull()

y.iloc[20:41,0:5]

y.loc[10:30,'team1':'possession team2']

y['team2'].value_counts()[30]

y['team1'].value_counts()

y.groupby(['team1','team2']).sum()

y.sort_values(by='team1')

y.isnull().sum()

y.replace('',np.nan)

y.isnull().sum()*100/len(y)

y.dropna()

y.dtypes

sns.histplot(data=y,hue=y['category'],x='number of goals team1',y='number of goals team2',bins=30)
plt.show()

y.describe()

y.value_counts('number of goals team1').mean()

sns.countplot(data=y,x='total attempts team1',hue=y['hour'])
plt.show()

sns.dogplot(data=y,x='total attempts team2')
plt.show()

y['team1'] = pd.to_numeric(y['team1'], errors='coerce')

plt.figure(figsize=(8,5))
sns.lineplot(data=y,x='total attempts team2',y='category',hue=y['hour'])
plt.show()

y.dtypes

y['penalties scored team1'].value_counts()

y['goal preventions team1'].value_counts()

sns.ecdfplot(data=y,x='goal preventions team1',hue=y['penalties scored team1'])
plt.show()

plt.figure(figsize=(8,4))
sns.displot(y['goal preventions team2'],kde=True)
plt.show()

sns.countplot(data=y,hue=y['own goals team1'],y='team2')
plt.show()

sns.kdeplot(data=y,x='goal preventions team1',y='goal preventions team2',hue=y['hour'])
sns.scatterplot(data=y,x='goal preventions team1',y='goal preventions team2',hue=y['own goals team2'])
sns.histplot(data=y,x='goal preventions team1',y='goal preventions team2',bins=20,pthresh=.1, cmap="mako")
plt.show()

sns.lineplot(data=y,x='forced turnovers team1',y='forced turnovers team2')
sns.set_theme(style='ticks')
plt.show()

y['defensive pressures applied team2'].value_counts()

plt.figure(figsize=(8,7))
plt.subplot(2,2,1)
sns.boxenplot(data=y,x='defensive pressures applied team1')
plt.xticks(rotation=60)
plt.subplot(2,2,2)
sns.boxplot(data=y,x='defensive pressures applied team2')
plt.xticks(rotation=60)
plt.show()

y.head(1)