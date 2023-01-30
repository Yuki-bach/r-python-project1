#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import collections


# 
# ## Dataset: World Happiness Report
# Source: https://www.kaggle.com/datasets/unsdsn/world-happiness<br>
# Year: 2015-2019<br>
# 156 countries
# 

# In[2]:


df = pd.read_csv("2019.csv")
df_2015 = pd.read_csv("2015.csv")
df_2016 = pd.read_csv("2016.csv")
df_2017 = pd.read_csv("2017.csv")
df_2018 = pd.read_csv("2018.csv")


# ### Change the column names

# In[3]:


df_2015.rename(columns={'Country': 'Country or region', 'Happiness Rank': 'Overall rank', 'Happiness Score': 'Score', 'Economy (GDP per Capita)': 'GDP per capita',
                        'Family': 'Social support', 'Health (Life Expectancy)': 'Healthy life expectancy'}, inplace=True)
df_2016.rename(columns={'Country': 'Country or region', 'Happiness Rank': 'Overall rank', 'Happiness Score': 'Score', 'Economy (GDP per Capita)': 'GDP per capita',
                        'Family': 'Social support', 'Health (Life Expectancy)': 'Healthy life expectancy'}, inplace=True)
df_2017.rename(columns={'Country': 'Country or region', 'Happiness.Rank': 'Overall rank', 'Happiness.Score': 'Score', 'Economy..GDP.per.Capita.': 'GDP per capita',
                        'Family': 'Social support', 'Health..Life.Expectancy.': 'Healthy life expectancy'}, inplace=True)
df_2019 = df


# In[4]:


df.head()


# 
# ### Terms Used in Dataset
# 
#  - GDP per capita:GDP per capita is a measure of a country's economic output that accounts for its number of people.<br>
#  - Social support:Social support means having friends and other people, including family, to turn to in times of need or crisis to give you a broader focus and positive self-image. Social support enhances quality of life and provides a buffer against adverse life events.<br>
#  - Healthy life expectancy:Healthy Life Expectancy is the average number of years that a newborn can expect to live in "full health"—in other words, not hampered by disabling illnesses or injuries.<br>
#  - Freedom to make life choices:Freedom of choice describes an individual's opportunity and autonomy to perform an action selected from at least two available options, unconstrained by external parties.<br>
#  - Generosity:the quality of being kind and generous.<br>
#  - Perceptions of corruption:The Corruption Perceptions Index (CPI) is an index published annually by Transparency International since 1995 which ranks countries "by their perceived levels of public sector corruption, as determined by expert assessments and opinion surveys.<br>

# ### Notes
# Basically, I take the same topic as Project 1, and do programming in Python.<br>
# In project 1, I used only 2019's data. The following codes, which use data from 2015 to 2018, are new additions to project2.

# ### Question: What Makes us Happy? 
# In recent years, there has been much sad news, including a coronavirus pandemic and a prolonged war in Ukraine.<br>
# The fast-changing news make us pessimistic. Thus, I want to know what makes us happy, and have a great time.
# 

# ### 1. Correlation heatmap
# 
# Happiness Score is a target.<br>
# The heatmap shows that GDP per capita, Social Support, and Health are correlated with Happiness Score.

# In[5]:


sns.heatmap(df[["Score", "GDP per capita", "Social support", "Healthy life expectancy", "Freedom to make life choices", "Generosity", "Perceptions of corruption"]].corr())


# ### 2. The top 10 countries
# 
# This bar plot also shows that GDP per capita, Social Support, and Health are major factors.<br>
# These three elements consist of 70% of total approximately.<br>
# "Social Support" seems the biggest proportion in the most top-10 countries.
# ##### Why do these three factors account for a large percentage in each country?

# In[6]:


def stackedBar(df, n):
    df.iloc[0:n, 3:9].set_index(df.iloc[0:n,1]).plot(kind='bar', stacked=True)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    
stackedBar(df.head(10) ,10)


# ### 3. Histogram of all 6 elements
# The histograms below answer the above question.<br>
# 
# Findings<br>
#  - The three graphs in the first row are wider and have larger maximum values than those in the second row.
#  - Especially, social support's peak is located to the right, so it is likely to be higher than other elements in each countries.<br>
#  - The shape of "Healthy life expectancy" is similar to "Social support."<br>
#  Therefore, 3 elements (GDP per capita, Social Support, and Health) tend to be higher than other elements.
#  ##### Is this trend only for 2019?

# In[7]:


fig, axes = plt.subplots(2, 3, sharex=True, sharey=True, figsize = (16,8))
index = 3
for i in range(2):
    for j in range(3):
        axes[i, j].hist(df.iloc[:, index])
        axes[i,j].set_ylabel(df.columns[index])
        index +=1


# ### Highest Score in Each Country in 2015-2019
# The bar chart below shows the number of highest score's element in each year. <br>
# The chart in 2016 is different from other charts. If we consider the 2016 data as an outlier, we see that social support is increasing and GDP per capita is decreasing.

# In[8]:


counter_2015 = collections.Counter(df_2015.iloc[:, 5:8].idxmax(axis=1))
highest_scores = pd.DataFrame.from_dict(counter_2015, orient='index')
highest_scores['2015'] = pd.DataFrame.from_dict(counter_2015, orient='index')

counter_2016 = collections.Counter(df_2016.iloc[:, 6:9].idxmax(axis=1))
highest_scores['2016'] = pd.DataFrame.from_dict(counter_2016, orient='index')

counter_2017 = collections.Counter(df_2017.iloc[:, 5:8].idxmax(axis=1))
highest_scores['2017'] = pd.DataFrame.from_dict(counter_2017, orient='index')

counter_2018 = collections.Counter(df_2018.iloc[:, 3:6].idxmax(axis=1))
highest_scores['2018'] = pd.DataFrame.from_dict(counter_2018, orient='index')

counter_2019 = collections.Counter(df_2019.iloc[:, 3:6].idxmax(axis=1))
highest_scores['2019'] = pd.DataFrame.from_dict(counter_2019, orient='index')


highest_scores = highest_scores.iloc[:, 1:].fillna(0)


# In[9]:


ax = highest_scores.transpose().plot(y=["GDP per capita", "Social support", "Healthy life expectancy"], kind="bar", rot=0, use_index=True)


# ## Answer
# Happiness was found to be related to multiple factors: GDP per capita, Social Support, and Health.
# In recent years, the importance for social support has increased.
# This survey was conducted on a national basis and not on an individual basis.
# To begin with, the feeling of happiness is a subjective thing that varies from person to person.
# In order to capture happiness objectively, each factor is scored.
# The data indicate that the three factors of GDP per capita, social support, and health are particularly important.
# Translated to individuals, their own productivity (earning), relationships with family and friends, and health are important.
# We can lead a fulfilling life by being aware of these factors.

# ## Appendix
# Finally, I analyze what my home country, Japan, needs to do to raise its happiness score.<br> As the below row shows, Japan's rank is 58. The score is almost 2 points lower than the first-place, Finland.

# In[10]:


df.head(1).append(df[df['Country or region']=="Japan"])


# ### Japan: 3rd highest "Healthy life expectancy" country
# It is higher than those of Finland. 

# In[11]:


df.sort_values("Healthy life expectancy", ascending=False).head(5)


# ### Japan and Top 5 Countries 
# Japanese score of top 3 elements is almost same as other top 5 countries. <br>
# However, other 3 elements is much lower than other countries. 

# In[12]:


df_japan = df.head(5).append(df[df['Country or region']=="Japan"])
stackedBar(df_japan, 6)


# ### Japan Ranking in 2015-2019
# Japanese rank had been decreasing. 

# In[13]:


japan_rank = np.zeros((5,2))
for i, year in enumerate(range(2015, 2020)):
    japan_rank[i] = globals()["df_%d" % year].loc[globals()["df_%d" % year]['Country or region']=="Japan", ["Overall rank"]]


# In[14]:


plt.plot(range(2015, 2020), japan_rank[:, 0:1])
plt.xticks(np.arange(2015, 2020))


# ## Additional Question: How much do happiness rankings change each year?
# ### Top 10 Countries in 2015-2019

# In[15]:


# Create a dataframe of ranking

df_ranking = df.iloc[0:10, 1:2]

for year in range(2015, 2020):
    ranking = np.zeros((10,2))
    for i in range(10):
        ranking[i] = globals()["df_%d" % year].loc[df_ranking.iloc[i, 0]==globals()["df_%d" % year]['Country or region'], ["Overall rank"]]   
    df_ranking["{0}".format(year)] = ranking[:,0]

df_ranking


# In[16]:


# plot
df_plot = df_ranking.iloc[:,2:6].transpose()

fig,ax = plt.subplots(figsize=(10,8))
ax.plot(df_plot)
ax.set_title("Top 10 Countries in 2015-2019")
ax.invert_yaxis()
ax.grid(axis="x")
ax.legend(df_ranking.iloc[:, 0],bbox_to_anchor=(1.1,0.97))
plt.yticks(np.arange(1, 14, 1.0))
plt.show()


# In[17]:


# Create a datafram
df_top10_scores = df.iloc[0:10, 1:2]

for year in range(2015, 2020):
    scores = np.zeros((10,2))
    for i in range(10):
        scores[i] = globals()["df_%d" % year].loc[df_top10_scores.iloc[i, 0]==globals()["df_%d" % year]['Country or region'], ["Score"]]   
    df_top10_scores["{0}".format(year)] = scores[:,0]
    
df_top10_scores = df_top10_scores.iloc[:,2:6].transpose()

# plot
fig,ax = plt.subplots(figsize=(10,8))
ax.plot(df_top10_scores)
ax.set_title("Score Transition in Top 10 Countries in 2015-2019")
ax.grid(axis="x")
ax.legend(df_ranking.iloc[:, 0],bbox_to_anchor=(1.1,0.97))
plt.yticks(np.arange(6.9, 7.8, 0.1))
plt.show()


# There are some fluctuations in the ranking. There are no examples of top ranking countries losing or gaining much ground. Finland's increase from 2017 to 2018 is the largest value (4).

# In[ ]:




