#!/usr/bin/env python
# coding: utf-8

# # Module 12 Challenge
# ## Deliverable 2: Scrape and Analyze Mars Weather Data

# In[1]:


# Import relevant libraries
from splinter import Browser
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


import os;
os.environ["PATH"] += os.pathsep + 'C:\\Users\\helin\\Downloads\\chromedriver_win32'


# In[3]:


browser = Browser('chrome')


# ### Step 1: Visit the Website
# 
# Use automated browsing to visit the [Mars Temperature Data Site](https://static.bc-edx.com/data/web/mars_facts/temperature.html). Inspect the page to identify which elements to scrape.
# 
#    > **Hint** To identify which elements to scrape, you might want to inspect the page by using Chrome DevTools to discover whether the table contains usable classes.
# 

# In[4]:


# Visit the website
# https://static.bc-edx.com/data/web/mars_facts/temperature.html
url = 'https://static.bc-edx.com/data/web/mars_facts/temperature.html'
browser.visit(url)


# ### Step 2: Scrape the Table
# 
# Create a Beautiful Soup object and use it to scrape the data in the HTML table.
# 
# Note that this can also be achieved by using the Pandas `read_html` function. However, use Beautiful Soup here to continue sharpening your web scraping skills.

# In[5]:


# Create a Beautiful Soup Object
html=browser.html
mars_soup=soup(html,'html.parser')
mars_soup


# In[6]:


# Extract all rows of data

# Find the table
table_rows = mars_soup.find_all('tr', class_='data-row')
table_rows


# In[7]:


mars_temp =[]


# Loop through the rows
for row in table_rows:
#row_heading = soup.find_all('th')
    row_data = row.find_all('td')
    row=[col.text for col in row_data]
    mars_temp.append(row)
 


# In[8]:


mars_temp


# In[9]:


mars_temp=pd.DataFrame(mars_temp)
mars_temp


# In[10]:


mars_temp.columns =(['id', 'terrestrial_date', 'sol', 'ls', 'month', 'min_temp','pressure'])
mars_temp


# ### Step 3: Store the Data
# 
# Assemble the scraped data into a Pandas DataFrame. The columns should have the same headings as the table on the website. Here’s an explanation of the column headings:
# 
# * `id`: the identification number of a single transmission from the Curiosity rover
# * `terrestrial_date`: the date on Earth
# * `sol`: the number of elapsed sols (Martian days) since Curiosity landed on Mars
# * `ls`: the solar longitude
# * `month`: the Martian month
# * `min_temp`: the minimum temperature, in Celsius, of a single Martian day (sol)
# * `pressure`: The atmospheric pressure at Curiosity's location

# In[11]:


# Create a Pandas DataFrame by using the list of rows and a list of the column names
df=pd.read_html('https://static.bc-edx.com/data/web/mars_facts/temperature.html')
mars_df=df[0]
mars_df


# In[12]:


mars_df.columns =(['id', 'terrestrial_date', 'sol', 'ls', 'month', 'min_temp','pressure'])
mars_df.dtypes


# # Confirm DataFrame was created successfully
# 
# 

# ### Step 4: Prepare Data for Analysis
# 
# Examine the data types that are currently associated with each column. If necessary, cast (or convert) the data to the appropriate `datetime`, `int`, or `float` data types.
# 
#   > **Hint** You can use the Pandas `astype` and `to_datetime` methods to accomplish this task.
# 

# In[13]:


# Change data types for data analysis
mars_df['terrestrial_date']=mars_df['terrestrial_date'].astype('datetime64')


# In[14]:


# Confirm type changes were successful by examining data types 
mars_df.dtypes


# ### Step 5: Analyze the Data
# 
# Analyze your dataset by using Pandas functions to answer the following questions:
# 
# 1. How many months exist on Mars?
# 2. How many Martian (and not Earth) days worth of data exist in the scraped dataset?
# 3. What are the coldest and the warmest months on Mars (at the location of Curiosity)? To answer this question:
#     * Find the average the minimum daily temperature for all of the months.
#     * Plot the results as a bar chart.
# 4. Which months have the lowest and the highest atmospheric pressure on Mars? To answer this question:
#     * Find the average the daily atmospheric pressure of all the months.
#     * Plot the results as a bar chart.
# 5. About how many terrestrial (Earth) days exist in a Martian year? To answer this question:
#     * Consider how many days elapse on Earth in the time that Mars circles the Sun once.
#     * Visually estimate the result by plotting the daily minimum temperature.
# 

# In[15]:


# 1. How many months are there on Mars?
month_count = mars_df["month"].nunique()
month_count


# In[16]:


# 2. How many Martian days' worth of data are there?
martiandays_count = mars_df["terrestrial_date"].count()

martiandays_count


# In[17]:


# 3. What is the average low temperature by month?
low_temp = mars_df.groupby(["month"]).mean()["min_temp"]
low_temp


# In[27]:


df_low = pd.DataFrame(low_temp, columns=['min_temp']).reset_index()
df_low


# In[28]:


# Plot the average temperature by month

low_temp.plot.bar(color="green", grid=False, figsize=(6,5),style='s-')
plt.title('Average Temperature by Month')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.xlim(-1,12)
plt.show()


# In[37]:


# Identify the coldest and hottest months in Curiosity's location
low_temp.sort_values().plot.bar(color="green", grid=False, figsize=(6,5))
plt.title('Average Temperature by Month')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.xlim(-1,12)
plt.show()


# In[21]:


# 4. Average pressure by Martian month
ave_pres = mars_df.groupby(["month"]).mean()["pressure"]
ave_pres


# In[36]:


# Plot the average pressure by month

ave_pres.plot.bar(color="green", grid=False, figsize=(6,5))
plt.title('Average Pressure by Month')
plt.xlabel('Month')
plt.ylabel('Pressure')
plt.xlim(-1,12)
plt.show()


# In[35]:


ave_pres.sort_values().plot.bar(color="green", grid=False, figsize=(6,5))
plt.title('Average Pressure by Month')
plt.xlabel('Month')
plt.ylabel('Pressure')
plt.xlim(-1,12)
plt.show()


# In[63]:


df = pd.DataFrame(mars_df, columns=['sol','min_temp','terrestrial_date']).reset_index()
df


# In[66]:


# 5. How many terrestrial (earth) days are there in a Martian year

df.plot.bar(color="green", grid=False, figsize=(6,5))
plt.title('Average Temperature by Month')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.show()


# On average, the third month has the coldest minimum temperature on Mars, and the eighth month is the warmest. But it is always very cold there in human terms!
# 
# 

# Atmospheric pressure is, on average, lowest in the sixth month and highest in the ninth.

# The distance from peak to peak is roughly 1425-750, or 675 days. A year on Mars appears to be about 675 days from the plot. Internet search confirms that a Mars year is equivalent to 687 earth days.

# ### Step 6: Save the Data
# 
# Export the DataFrame to a CSV file.

# In[24]:


# Write the data to a CSV
mars_df.to_csv(index=False)


# In[25]:


browser.quit()


# In[ ]:




