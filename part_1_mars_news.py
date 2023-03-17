#!/usr/bin/env python
# coding: utf-8

# # Module 12 Challenge
# ## Deliverable 1: Scrape Titles and Preview Text from Mars News

# In[1]:


import os;
os.environ["PATH"] += os.pathsep + 'C:\\Users\\helin\\Downloads\\chromedriver_win32'


# In[2]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup


# In[3]:


browser = Browser('chrome')


# ### Step 1: Visit the Website
# 
# 1. Use automated browsing to visit the [Mars news site](https://static.bc-edx.com/data/web/mars_news/index.html). Inspect the page to identify which elements to scrape.
# 
#       > **Hint** To identify which elements to scrape, you might want to inspect the page by using Chrome DevTools.

# In[4]:


# Visit the Mars news site: https://static.bc-edx.com/data/web/mars_news/index.html
url='https://static.bc-edx.com/data/web/mars_news/index.html'
browser.visit(url)


# ### Step 2: Scrape the Website
# 
# Create a Beautiful Soup object and use it to extract text elements from the website.

# In[5]:


# Create a Beautiful Soup object
html=browser.html
soup=soup(html, 'html.parser')


# In[6]:


# Extract all the text elements
all_titles = soup.find_all("div", class_="content_title")
all_titles


# ### Step 3: Store the Results
# 
# Extract the titles and preview text of the news articles that you scraped. Store the scraping results in Python data structures as follows:
# 
# * Store each title-and-preview pair in a Python dictionary. And, give each dictionary two keys: `title` and `preview`. An example is the following:
# 
#   ```python
#   {'title': "NASA's MAVEN Observes Martian Light Show Caused by Major Solar Storm", 
#    'preview': "For the first time in its eight years orbiting Mars, NASA’s MAVEN mission witnessed two different types of ultraviolet aurorae simultaneously, the result of solar storms that began on Aug. 27."
#   }
#   ```
# 
# * Store all the dictionaries in a Python list.
# 
# * Print the list in your notebook.

# In[7]:


# Create an empty list to store the dictionaries
titles_prev= soup.find_all("div", class_="article_teaser_body")
titles_prev


# In[19]:


title_prev_dict={}


# In[40]:


# Loop through the text elements
# Extract the title and preview text from the elements
# Store each title and preview pair in a dictionary
# Add the dictionary to the list
all_divs =soup.find_all("div")
for div in all_divs:
    title= soup.find("div", class_="content_title").text
    preview=soup.find("div", class_="article_teaser_body").text
    title_prev_dict= {'title': title,
                      'preview': preview}
 


# In[41]:


# Print the list to confirm success
print(title_prev_dict)


# In[11]:


browser.quit()


# In[ ]:




