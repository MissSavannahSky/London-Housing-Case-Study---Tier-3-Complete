#!/usr/bin/env python
# coding: utf-8

# # London Housing Case Study - Tier 3 Complete
# 
# ## Objectives
# Hey! Great job getting through those challenging DataCamp courses. You're learning a lot in a short span of time. 
# 
# In this notebook, you're going to apply the skills you've been learning, bridging the gap between the controlled environment of DataCamp and the *slightly* messier work that data scientists do with actual datasets!
# 
# Here’s the mystery we’re going to solve: ***which boroughs of London have seen the greatest increase in housing prices, on average, over the last two decades?***
# 
# 
# A borough is just a fancy word for district. You may be familiar with the five boroughs of New York… well, there are 32 boroughs within Greater London [(here's some info for the curious)](https://en.wikipedia.org/wiki/London_boroughs). Some of them are more desirable areas to live in, and the data will reflect that with a greater rise in housing prices.
# 
# ***This is the Tier 3 notebook, which means it's not filled in at all: we'll just give you the skeleton of a project, the brief and the data. It's up to you to play around with it and see what you can find out! Good luck! If you struggle, feel free to look at easier tiers for help; but try to dip in and out of them, as the more independent work you do, the better it is for your learning!***
# 
# This challenge will make use of only what you learned in the following DataCamp courses: 
# - Prework courses (Introduction to Python for Data Science, Intermediate Python for Data Science)
# - Data Types for Data Science
# - Python Data Science Toolbox (Part One) 
# - pandas Foundations
# - Manipulating DataFrames with pandas
# - Merging DataFrames with pandas
# 
# Of the tools, techniques and concepts in the above DataCamp courses, this challenge should require the application of the following: 
# - **pandas**
#     - **data ingestion and inspection** (pandas Foundations, Module One) 
#     - **exploratory data analysis** (pandas Foundations, Module Two)
#     - **tidying and cleaning** (Manipulating DataFrames with pandas, Module Three) 
#     - **transforming DataFrames** (Manipulating DataFrames with pandas, Module One)
#     - **subsetting DataFrames with lists** (Manipulating DataFrames with pandas, Module One) 
#     - **filtering DataFrames** (Manipulating DataFrames with pandas, Module One) 
#     - **grouping data** (Manipulating DataFrames with pandas, Module Four) 
#     - **melting data** (Manipulating DataFrames with pandas, Module Three) 
#     - **advanced indexing** (Manipulating DataFrames with pandas, Module Four) 
# - **matplotlib** (Intermediate Python for Data Science, Module One)
# - **fundamental data types** (Data Types for Data Science, Module One) 
# - **dictionaries** (Intermediate Python for Data Science, Module Two)
# - **handling dates and times** (Data Types for Data Science, Module Four)
# - **function definition** (Python Data Science Toolbox - Part One, Module One)
# - **default arguments, variable length, and scope** (Python Data Science Toolbox - Part One, Module Two) 
# - **lambda functions and error handling** (Python Data Science Toolbox - Part One, Module Four) 

# ## The Data Science Pipeline
# 
# This is Tier Three, so we'll get you started. But after that, it's all in your hands! When you feel done with your investigations, look back over what you've accomplished, and prepare a quick presentation of your findings for the next mentor meeting. 
# 
# Data Science is magical. In this case study, you'll get to apply some complex machine learning algorithms. But as  [David Spiegelhalter](https://www.youtube.com/watch?v=oUs1uvsz0Ok) reminds us, there is no substitute for simply **taking a really, really good look at the data.** Sometimes, this is all we need to answer our question.
# 
# Data Science projects generally adhere to the four stages of Data Science Pipeline:
# 1. Sourcing and loading 
# 2. Cleaning, transforming, and visualizing 
# 3. Modeling 
# 4. Evaluating and concluding 
# 

# ### 1. Sourcing and Loading 
# 
# Any Data Science project kicks off by importing  ***pandas***. The documentation of this wonderful library can be found [here](https://pandas.pydata.org/). As you've seen, pandas is conveniently connected to the [Numpy](http://www.numpy.org/) and [Matplotlib](https://matplotlib.org/) libraries. 
# 
# ***Hint:*** This part of the data science pipeline will test those skills you acquired in the pandas Foundations course, Module One. 

# #### 1.1. Importing Libraries

# In[1]:


# Let's import the pandas, numpy libraries as pd, and np respectively. 
import pandas as pd
import numpy as np

# Load the pyplot collection of functions from matplotlib, as plt 
import matplotlib.pyplot as plt


# #### 1.2.  Loading the data
# Your data comes from the [London Datastore](https://data.london.gov.uk/): a free, open-source data-sharing portal for London-oriented datasets. 

# In[2]:


# First, make a variable called url_LondonHousePrices, and assign it the following link, enclosed in quotation-marks as a string:
# https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls

url_LondonHousePrices = "https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls"

# The dataset we're interested in contains the Average prices of the houses, and is actually on a particular sheet of the Excel file. 
# As a result, we need to specify the sheet name in the read_excel() method.
# Put this data into a variable called properties.  
properties = pd.read_excel(url_LondonHousePrices, sheet_name='Average price', index_col= None, header=0)


# ### 2. Cleaning, transforming, and visualizing
# This second stage is arguably the most important part of any Data Science project. The first thing to do is take a proper look at the data. Cleaning forms the majority of this stage, and can be done both before or after Transformation.
# 
# The end goal of data cleaning is to have tidy data. When data is tidy: 
# 
# 1. Each variable has a column.
# 2. Each observation forms a row.
# 
# Keep the end goal in mind as you move through this process, every step will take you closer. 
# 
# 
# 
# ***Hint:*** This part of the data science pipeline should test those skills you acquired in: 
# - Intermediate Python for data science, all modules.
# - pandas Foundations, all modules. 
# - Manipulating DataFrames with pandas, all modules.
# - Data Types for Data Science, Module Four.
# - Python Data Science Toolbox - Part One, all modules

# **2.1. Exploring your data** 
# 
# Think about your pandas functions for checking out a dataframe. 

# In[3]:


properties.shape
properties.head()


# **2.2. Cleaning the data**
# 
# You might find you need to transpose your dataframe, check out what its row indexes are, and reset the index. You  also might find you need to assign the values of the first row to your column headings  . (Hint: recall the .columns feature of DataFrames, as well as the iloc[] method).
# 
# Don't be afraid to use StackOverflow for help  with this.

# In[4]:


properties_T = properties.T
properties_T.head()


# In[5]:


properties_T.index


# In[6]:


properties_T = properties_T.reset_index()


# In[7]:


properties_T.index


# In[8]:


properties_T.columns


# In[9]:


properties_T.head()


# In[10]:


properties_T.iloc[[0]]


# In[11]:


properties_T.columns = properties_T.iloc[0]


# In[12]:


properties_T.head()


# In[13]:


properties_T = properties_T.drop(0)


# In[14]:


properties_T.head()


# **2.3. Cleaning the data (part 2)**
# 
# You might we have to **rename** a couple columns. How do you do this? The clue's pretty bold...

# In[15]:


properties_T = properties_T.rename(columns = {'Unnamed: 0':'London_Borough', pd.NaT: 'ID'})
properties_T.head()


# **2.4.Transforming the data**
# 
# Remember what Wes McKinney said about tidy data? 
# 
# You might need to **melt** your DataFrame here. 

# In[20]:


clean_properties = pd.melt(properties_T, id_vars= ['London_Borough', 'ID'])


# Remember to make sure your column data types are all correct. Average prices, for example, should be floating point numbers... 

# In[21]:


clean_properties.head()


# In[22]:


clean_properties = clean_properties.rename(columns = {0: 'Month', 'value': 'Average_price'})


# In[23]:


clean_properties.head()


# In[26]:


clean_properties.dtypes


# In[28]:


clean_properties['Average_price'] = pd.to_numeric(clean_properties['Average_price'])


# In[29]:


clean_properties.dtypes


# In[30]:


clean_properties.count()


# **2.5. Cleaning the data (part 3)**
# 
# Do we have an equal number of observations in the ID, Average Price, Month, and London Borough columns? Remember that there are only 32 London Boroughs. How many entries do you have in that column? 
# 
# Check out the contents of the London Borough column, and if you find null values, get rid of them however you see fit. 

# In[31]:


clean_properties['London_Borough'].unique()


# In[32]:


clean_properties[clean_properties['London_Borough'] == 'Unnamed: 34'].head()


# In[33]:


clean_properties[clean_properties['London_Borough'] == 'Unnamed: 37'].head()


# In[34]:


clean_properties[clean_properties['ID'].isna()]


# In[35]:


NaNFreeDF1 = clean_properties[clean_properties['Average_price'].notna()]


# In[36]:


NaNFreeDF1.head(48)


# In[37]:


NaNFreeDF2 = clean_properties.dropna()


# In[38]:


NaNFreeDF2.head(48)


# In[39]:


NaNFreeDF2['London_Borough'].unique()


# In[40]:


print(clean_properties.shape)


# In[41]:


print(NaNFreeDF1.shape)


# In[42]:


print(NaNFreeDF2.shape)


# In[43]:


nonBoroughs = ['Inner London', 'Outer London', 
               'NORTH EAST', 'NORTH WEST', 'YORKS & THE HUMBER', 
               'EAST MIDLANDS', 'WEST MIDLANDS',
              'EAST OF ENGLAND', 'LONDON', 'SOUTH EAST', 
              'SOUTH WEST', 'England']


# In[44]:


NaNFreeDF2[NaNFreeDF2.London_Borough.isin(nonBoroughs)]


# In[45]:


NaNFreeDF2[~NaNFreeDF2.London_Borough.isin(nonBoroughs)]


# In[46]:


NaNFreeDF2 = NaNFreeDF2[~NaNFreeDF2.London_Borough.isin(nonBoroughs)]


# In[47]:


NaNFreeDF2.head()


# In[49]:


df = NaNFreeDF2


# In[50]:


df.head()


# In[51]:


df.dtypes


# **2.6. Visualizing the data**
# 
# To visualize the data, why not subset on a particular London Borough? Maybe do a line plot of Month against Average Price?

# In[65]:


camden_prices = df[df['London_Borough'] == 'Camden']


# In[66]:


ax = camden_prices.plot(kind ='line', x = 'Month', y='Average_price')


# In[67]:


ax.set_ylabel('price')


# To limit the number of data points you have, you might want to extract the year from every month value your *Month* column. 
# 
# To this end, you *could* apply a ***lambda function***. Your logic could work as follows:
# 1. look through the `Month` column
# 2. extract the year from each individual value in that column 
# 3. store that corresponding year as separate column. 
# 
# Whether you go ahead with this is up to you. Just so long as you answer our initial brief: which boroughs of London have seen the greatest house price increase, on average, over the past two decades? 

# In[75]:


df['Year'] = df['Month'].apply(lambda t: t.year)


# In[76]:


df.tail()


# In[77]:


dfg = df.groupby(by=['London_Borough', 'Year']).mean()


# In[78]:


dfg.sample(10)


# In[79]:


dfg = dfg.reset_index()


# In[80]:


dfg.head()


# **3. Modeling**
# 
# Consider creating a function that will calculate a ratio of house prices, comparing the price of a house in 2018 to the price in 1998.
# 
# Consider calling this function create_price_ratio.
# 
# You'd want this function to:
# 1. Take a filter of dfg, specifically where this filter constrains the London_Borough, as an argument. For example, one admissible argument should be: dfg[dfg['London_Borough']=='Camden'].
# 2. Get the Average Price for that Borough, for the years 1998 and 2018.
# 4. Calculate the ratio of the Average Price for 1998 divided by the Average Price for 2018.
# 5. Return that ratio.
# 
# Once you've written this function, you ultimately want to use it to iterate through all the unique London_Boroughs and work out the ratio capturing the difference of house prices between 1998 and 2018.
# 
# Bear in mind: you don't have to write a function like this if you don't want to. If you can solve the brief otherwise, then great! 
# 
# ***Hint***: This section should test the skills you acquired in:
# - Python Data Science Toolbox - Part One, all modules

# In[82]:


def create_price_ratio(d):
    y1998 = float(d['Average_price'][d['Year']==1998])
    y2018 = float(d['Average_price'][d['Year']==2018])
    ratio = [y2018/y1998]
    return ratio


# In[83]:


create_price_ratio(dfg[dfg['London_Borough']=='Barking & Dagenham'])


# In[84]:


final = {}


# In[85]:


for b in dfg['London_Borough'].unique():
    borough = dfg[dfg['London_Borough'] == b]
    final[b] = create_price_ratio(borough)


# In[86]:


print(final)


# In[87]:


df_ratios = pd.DataFrame(final)


# In[88]:


df_ratios.head()


# In[89]:


df_ratios_T = df_ratios.T


# In[90]:


df_ratios = df_ratios_T.reset_index()


# In[91]:


df_ratios.head()


# In[96]:


df_ratios.rename(columns={'index':'Borough', 0:'2018'}, inplace=True)


# In[97]:


df_ratios.head()


# In[98]:


top15 = df_ratios.sort_values(by = '2018', ascending = False).head(15)


# In[99]:


print(top15)


# In[100]:


ax = top15[['Borough','2018']].plot(kind='bar')


# In[101]:


ax.set_xticklabels(top15.Borough)


# ### 4. Conclusion
# What can you conclude? Type out your conclusion below. 
# 
# Look back at your notebook. Think about how you might summarize what you have done, and prepare a quick presentation on it to your mentor at your next meeting. 
# 
# We hope you enjoyed this practical project. It should have consolidated your data hygiene and pandas skills by looking at a real-world problem involving just the kind of dataset you might encounter as a budding data scientist. Congratulations, and looking forward to seeing you at the next step in the course! 
