#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Libraries
import numpy as np
import pandas as pd
import plotly as py
import plotly.express as px
import plotly.graph_objs as go
import seaborn as sns
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)


# In[24]:


# Read Data
df = pd.read_csv('covid_impact_on_airport_traffic.csv')


# In[25]:


# Checking dataframe details
df.head()


# In[26]:


# Sort by dates and get overall airport traffic  by country
df_country = df.groupby(['Date', 'Country']).sum().reset_index().sort_values('Date', ascending=False)


# In[27]:


df_country


# In[28]:


df_country.drop('Version', axis=1, inplace=True)


# In[29]:


# Create Choropleth
fig = data = px.choropleth(df_country,
    locations = "Country",
    locationmode = "country names",
    hover_name="Country",
    color="PercentOfBaseline",
    animation_frame="Date"
)


# In[30]:


fig.update_layout(
    title_text = 'COVID-19\'s Impact on Airport Traffic Worldwide',
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    )
)

fig.show()


# ### Impact on American Airports

# In[31]:


# Filter american airports and sort by date
df_states = df[df['Country'] == 'United States of America (the)'].groupby(['Date', 'State']).sum().reset_index().sort_values('Date', ascending=True)


# In[32]:


df_states


# In[33]:


# State codes dictionary
state_codes = {
    'District of Columbia' : 'dc','Mississippi': 'MS', 'Oklahoma': 'OK', 
    'Delaware': 'DE', 'Minnesota': 'MN', 'Illinois': 'IL', 'Arkansas': 'AR', 
    'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA', 
    'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ', 
    'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT', 
    'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT', 
    'California': 'CA', 'Massachusetts': 'MA', 'West Virginia': 'WV', 
    'South Carolina': 'SC', 'New Hampshire': 'NH', 'Wisconsin': 'WI',
    'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND', 
    'Pennsylvania': 'PA', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY', 
    'Hawaii': 'HI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH', 
    'Alabama': 'AL', 'Rhode Island': 'RI', 'South Dakota': 'SD', 
    'Colorado': 'CO', 'New Jersey': 'NJ', 'Washington': 'WA', 
    'North Carolina': 'NC', 'New York': 'NY', 'Texas': 'TX', 
    'Nevada': 'NV', 'Maine': 'ME'}

# Create abbreviation column
df_states['state_code'] = df_states['State'].apply(lambda x : state_codes[x])


# In[34]:


df_states


# In[35]:


# Create Choropleth
fig = data = px.choropleth(df_states,
    locations = "state_code",
    locationmode = "USA-states",
    hover_name="State",
    color="PercentOfBaseline",
    animation_frame="Date",
)


# In[36]:


fig.update_layout(
    title_text = 'COVID-19\'s Impact on American Airports',
    title_x = 0.5,
    geo_scope='usa'
)

fig.show()


# In[37]:


from datetime import date

# Change Date format from strng to date
df["Date"] = df["Date"].map(lambda x: date.fromisoformat(x))


# In[38]:


df_month = pd.DataFrame(df["Date"].map(lambda d: d.month).value_counts())
df_month = df_month.reset_index()
df_month = df_month.rename(columns={"Date":"count", "index":"month"})
g = sns.barplot(data=df_month.reset_index(), y="count", x="month")
g.set_xticklabels(g.get_xticklabels(), rotation=90)
g.set_title("records for each month")


# In[ ]:




