#!/usr/bin/env python
# coding: utf-8

# POL 373: Campaigns and Elections
# 
# Data Analysis for CO-08
# 
# Matthew Bevivino

# In[81]:


# We begin by importing the necessary packages
import numpy as np
import pandas as pd
import os 
import matplotlib.pyplot as plt


# In[82]:


# We read in our data 
Colorado_DataFrame = pd.read_excel('C:/Users/mbevi/OneDrive/Documents/ColaradoDataFinal.xlsx')


# ## Note on variables and data collection: 
# 
# Our data comes formatted in an excel spreadsheet and was collected from various sources. 
# 
# Demographic Information by county (Race, Education, Income) was collected via the public U.S. Census colorado webpage
# linked below: 
# 
# https://www.census.gov/quickfacts/CO
# 
# Election totals by county for the 2016 and 2020 Presidential Election(s) from Politico. 
# 
# https://www.politico.com/2016-election/results/map/president/
# https://www.politico.com/2020-election/results/colorado/
# 
# Election totals for the Governor's race(s) came via Politico as well:
# 
# https://www.politico.com/election-results/2018/colorado/governor/

# In[83]:


# We will take a basic look at our data frame


# In[84]:


Colorado_DataFrame.info()
# Let's look at the first 15 observations
Colorado_DataFrame.head(n=15)


# From the first look at our dataset, we can see clearly what kind of variables we are working with. 
# 
# We can see Adams County in our Data Frame. Let's filter now to look at the three counties that will be included in CO-08. Adams, Weld, and Larimer. 
# 

# In[106]:


Colorado_DataFrame.loc[Colorado_DataFrame['County_Name'] == 'Adams ']

# Below we can now see information regarding Adams county


# In[105]:


Colorado_DataFrame.loc[Colorado_DataFrame['County_Name'] == 'Weld']

# Below we can now see information regarding Weld county


# In[87]:


Colorado_DataFrame.loc[Colorado_DataFrame['County_Name'] == 'Larimer']

# Below we can now see information regarding Larimer county


# Now, we will compare the data from these three counties to statewide and nationwide numbers for the same variables. 

# In[88]:


Colorado_DataFrame.loc[Colorado_DataFrame['County_Name'] == 'Statewide']


# In[89]:


Colorado_DataFrame.loc[Colorado_DataFrame['County_Name'] == 'United_States']


# We can see just from filtering out certain observations that the three counties we are interested in are unique demographically.
# 
# 
# Next step: Let's visualize some data. We will start with visualizing the relationship between Education and Democratic vote totals in the two prior Presidential Elections. 

# In[108]:


plt.scatter(Colorado_DataFrame['Bachelors_orHigher'], Colorado_DataFrame['Clinton2016'])
plt.scatter(Colorado_DataFrame['Bachelors_orHigher'], Colorado_DataFrame['Biden2020'])
plt.xlabel('Percent of population with Bachelors Degree or Higher')
plt.ylabel('Democratic Vote Share for President')


# Note: 2016 observations are in blue and 2020 observations are in orange. 

# Both visualizations above clearly reflect a positive correlation (albeit a vague one) between a college education and share that the Democratic party gets. We will proceed further with factors such as race and income.

# In[113]:


plt.scatter(Colorado_DataFrame['Hisp_Lat_Percent'], Colorado_DataFrame['Clinton2016'])
plt.scatter(Colorado_DataFrame['Hisp_Lat_Percent'], Colorado_DataFrame['Biden2020'])
plt.xlabel('Percent of population that identifies as Hispanic or Latino')
plt.ylabel('Democratic Vote Share for President')


# In[111]:


plt.scatter(Colorado_DataFrame['AfrAmer_percent'], Colorado_DataFrame['Clinton2016'])
plt.scatter(Colorado_DataFrame['AfrAmer_percent'], Colorado_DataFrame['Biden2020'])
plt.xlabel('Percentage of Population identifying as African American')
plt.ylabel('Democratic Vote Share for President')


# We do not see a large amount of Democratic (or Republican) allegience amongst African American voters in Colorado.

# We can see there is not much true correlation when we explore the relationship between Hispanic percentage of population and Democratic vote share. Interesting! We keep going with variables such as income per capita and median household income: 

# In[112]:


plt.scatter(Colorado_DataFrame['PerCapitaIncome'], Colorado_DataFrame['Clinton2016'])
plt.scatter(Colorado_DataFrame['PerCapitaIncome'], Colorado_DataFrame['Biden2020'])
plt.xlabel('Per-Capita Income')
plt.ylabel('Democratic Vote Share for President')


# In[99]:


plt.scatter(Colorado_DataFrame['HouseHoldIncome'], Colorado_DataFrame['Clinton2016'])
plt.scatter(Colorado_DataFrame['HouseHoldIncome'], Colorado_DataFrame['Biden2020'])


# ## What does this tell us? 
# So far, we have made scatterplots to represent the correlation between the Democratic vote share in both the 2016 and 2020 Presidential elections. These visualizations reveal the most meaningful correlation to be regarding Education level. Counties that have a significant amount of voters with a bachelors degree or higher are more likely to have higher Democratic vote shares. 
# 
# The relationship between Hispanic/Latin percentage of population and Democratic vote share may surprise the conventional wisdom. While Democrats are expected to possess a significant advantage over non-white voters, perhaps our analysis shows this advantage is less-so than expected. 

# # Win Number Calculation 

# ### Since this is a new congressional district, there is a lot of uncertainty with regards to turnout.
# ### We have to account for this uncertainty. 
# #### Under normal circumstances, if we had data from prior "similar" elections, we could use conventional means to find the "win number". Here, we will 
# #### Data on Adams County election results found via county clerk website:
# 
# https://www.adamsvotes.com/past-elections/#PastElections
# 
# #### Data on Weld County election results found via county clerk website:
# 
# https://www.weldgov.com/Home
# 
# #### Data on Larimer County election results found via county clerk website: 
# 
# https://www.larimer.gov/sites/default/files/uploads/2019/2018-general-electionsovc_web_0.pdf
# 
# 
# 

# In[142]:


# We will assign values to variables based on votes cast in the 2018 Colorado Governors race

Adams2018 = 174417
Weld2018 = 125372
Larimer2018 = 184021 

TotalVotes = Adams2018 + Weld2018 + Larimer2018

# We multiply TotalVotes by 0.52 to get win number

WinNumber = 0.52*TotalVotes

# To account for uncertainty, we will calculate a lower and upper bound. 

LowerBoundWinNumber = 0.7*WinNumber
UpperBoundWinNumber = 1.3*WinNumber 

n = int(TotalVotes **(1/2))
print(LowerBoundWinNumber)
print(UpperBoundWinNumber)
print(WinNumber)


# We now have out upper and lower bounds for our win number. We will now create a normal distribution and visualize it in order to show us a specified range of where our win number may lie. 

# In[140]:


Distribution = np.random.normal(loc=WinNumber, scale=, size=n)


# In[141]:


plt.hist(Distribution)


# The lower bound of our expected win number would be 176106. The upper bound would be 327055.
# The conventional definiton of the win number (AKA 0.52 times turnout number) would be 251581. 

# In[ ]:




