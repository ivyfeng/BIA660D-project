
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
#select works to select from an item
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as BS
import numpy as np
import pandas as pd
from selenium.common.exceptions import NoSuchElementException


# In[2]:


import random
import time
start_time = time.time()
normal_delay = random.normalvariate(2, 0.5)
time.sleep(normal_delay)    
# print("--- %.5f seconds ---" % (time.time() - start_time))

def delay(t):
    normal_delay = random.normalvariate(t, 0.5)
    time.sleep(normal_delay)


# In[3]:


driver = webdriver.Chrome('D:\ChromeDriver\chromedriver.exe')


# In[4]:


driver.get('https://www.amazon.com/RockBirds-Tactical-Flashlights-Fluorescent-Ring/dp/B00X61AJYM/ref=cm_cr_arp_d_product_top?ie=UTF8&th=1')


# In[5]:


# spot [see all customer reviews]
all_cust_reviews_div = driver.find_element_by_id('reviewSummary')
all_cust_reviews_link = driver.find_element_by_id('dp-summary-see-all-reviews')
all_cust_reviews_link.click()


# In[6]:


# current page to HTML
all_cust_reviews_page = driver.page_source
all_cust_reviews_soup = BS(all_cust_reviews_page, 'html5lib')


# In[7]:


#get div containing all reviews body
reviews_soup_div = all_cust_reviews_soup.find('div', attrs={'id':'cm_cr-review_list'})
reviews_soup_div_data = reviews_soup_div.find_all('div', attrs={'class': 'a-section review'})
num_of_reviews = len(reviews_soup_div_data)
# for loop through reviews_soup_div_data
score_list = []
title_list = []
review_list = []
date_list =[]
for i in range(0, num_of_reviews):
    review = reviews_soup_div_data[i].find('div', attrs={'class': 'a-section celwidget'})
    # retrieve title score and append it to score_list
    score = review.find('a', attrs={'class': 'a-link-normal'})['title']
    score_list.append(score)
    # retrieve title and append it to title_list
    title = review.find('a', attrs={'data-hook': 'review-title'}).get_text()
    title_list.append(title)
    # get review data and store in review_list
    review_body = review.find('span', attrs={'data-hook': 'review-body'}).get_text()
    review_list.append(review_body)
    # retrieve date
    date = review.find('span', attrs={'data-hook': 'review-date'}).get_text().encode("utf-8")
    date_list.append(date)


# In[8]:


reviews = pd.DataFrame({'Title':title_list,'Review_Content':review_list,'Score':score_list,'Date':date_list})
reviews[:5]


# In[22]:


import json
#reviews.to_json(orient='split')

