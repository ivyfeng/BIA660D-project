from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random
import time
import pandas as pd
import requests
import bs4

# In[29]:


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('http://www.mlb.com')

# In[30]:


stats_header_bar = driver.find_element_by_class_name('megamenu-static-navbar__menu-item--stats')

# In[31]:


stats_header_bar.click()

# In[32]:


season_2015_select = driver.find_element_by_xpath('//*[@id="sp_hitting_season"]/option[4]')

# In[33]:


season_2015_select.click()

# In[34]:


team_bar = driver.find_element_by_xpath('//*[@id="st_parent"]')

# In[35]:


team_bar.click()

# In[36]:


regular_season = driver.find_element_by_css_selector('#st_hitting_game_type > option:nth-child(1)')

# In[37]:


regular_season.click()

# In[38]:


normal_delay = random.normalvariate(2, 0.5)
time.sleep(normal_delay)

# In[39]:


time.sleep(8)
data_div = driver.find_element_by_id('datagrid')
data_html = data_div.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, "html5lib")
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df_home_run = pd.DataFrame(columns=head)

# In[40]:


context_table_q1 = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        context_table_q1.append(a.text)

# In[41]:


context_table_q1_prettify = []
for i in range(int(len(context_table_q1) / len(head))):
    s = context_table_q1[i * len(head): (i + 1) * len(head)]
    context_table_q1_prettify.append(s)

# In[42]:


context_table_q1_prettify
for i in range(30):
    df_home_run.loc[i] = context_table_q1_prettify[i]

df_home_run.drop("", axis=1)

# In[43]:


df_home_run.to_csv('C:\BIA Sycn\BIA660\Question_1.csv')

# In[44]:


df_home_run.sort_values(by=['HR'], ascending=False)

# In[45]:


highest_hr_team_name = df_home_run.iloc[1, 1]
highest_hr_team_name

# # Question 2-a

# In[56]:


## for AL
AL_bar = driver.find_element_by_xpath('//*[@id="st_hitting-0"]/fieldset[2]/label[2]/span')
AL_bar.click()

# In[59]:


time.sleep(5)
data_div_AL = driver.find_element_by_id('datagrid')
data_html_AL = data_div_AL.get_attribute('innerHTML')
AL_soup = bs4.BeautifulSoup(data_html_AL, "html5lib")
AL_head = [t.text.replace("▼", "") for t in AL_soup.thead.find_all("th")]
df_home_run_AL = pd.DataFrame(columns=AL_head)

# In[62]:


table_q2_a_AL = []
for t in soup_AL.tbody.find_all("tr"):
    for a in t.find_all("td"):
        table_q2_a_AL.append(a.text)

table_q2_a_AL_prettify = []
for i in range(int(len(table_q2_a_AL) / len(AL_head))):
    s = table_q2_a_AL[i * len(AL_head): (i + 1) * len(AL_head)]
    table_q2_a_AL_prettify.append(s)

table_q2_a_AL_prettify
for i in range(15):
    df_home_run_AL.loc[i] = table_q2_a_AL_prettify[i]

# In[51]:


df_home_run_AL.to_csv('C:\BIA Sycn\BIA660\Question_2.csv')

# In[63]:


al_data = pd.read_csv('C:\BIA Sycn\BIA660\Question_2.csv')
al_mean_hr = al_data['HR'].mean()
print(al_mean_hr)

# In[64]:


# for NL
NL_bar = driver.find_element_by_css_selector(
    '#st_hitting-0 > fieldset:nth-child(2) > label:nth-child(6) > span:nth-child(1)')
NL_bar.click()

# In[67]:


time.sleep(5)
data_div_NL = driver.find_element_by_id('datagrid')
data_html_NL = data_div_NL.get_attribute('innerHTML')
NL_soup = bs4.BeautifulSoup(data_html_NL, "html5lib")
NL_head = [t.text.replace("▼", "") for t in NL_soup.thead.find_all("th")]
df_home_run_NL = pd.DataFrame(columns=NL_head)

table_q2_a_NL = []
for t in NL_soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        table_q2_a_NL.append(a.text)

table_q2_a_NL_prettify = []
for i in range(int(len(table_q2_a_NL) / len(NL_head))):
    s = table_q2_a_NL[i * len(NL_head): (i + 1) * len(NL_head)]
    table_q2_a_NL_prettify.append(s)

for i in range(15):
    df_home_run_NL.loc[i] = table_q2_a_NL_prettify[i]

# In[68]:


df_home_run_NL.to_csv('C:\BIA Sycn\BIA660\Question_2_a_NL.csv')

# In[70]:


nl_data = pd.read_csv('C:\BIA Sycn\BIA660\Question_2_a_NL.csv')
nl_mean_hr = nl_data['HR'].mean()
print(nl_mean_hr)

# In[72]:


if al_mean_hr >= nl_mean_hr:
    print("The league with greatest avg num of homerun:AL ", al_mean_hr)
else:
    print("The league with greatest avg num of homerun:NL ", nl_mean_hr)

# # Question 2-b

# In[73]:


AL_bar = driver.find_element_by_xpath('//*[@id="st_hitting-0"]/fieldset[2]/label[2]/span')
AL_bar.click()

# In[74]:


time.sleep(10)
hitting_splits_element = driver.find_element_by_id('st_hitting_hitting_splits')
splits_select = Select(hitting_splits_element)
splits_select.select_by_visible_text('First Inning')

# In[77]:


time.sleep(5)
data_div_AL = driver.find_element_by_id('datagrid')
data_html_AL = data_div_AL.get_attribute('innerHTML')
soup_AL = bs4.BeautifulSoup(data_html_AL, "html5lib")
head_AL = [t.text.replace("▼", "") for t in soup_AL.thead.find_all("th")]
df_home_run_AL_b = pd.DataFrame(columns=head_AL)

table_q2_a_AL = []
for t in soup_AL.tbody.find_all("tr"):
    for a in t.find_all("td"):
        table_q2_a_AL.append(a.text)

table_q2_a_AL_prettify = []
for i in range(int(len(context_table_q2_a_AL) / len(head_AL))):
    s = table_q2_a_AL[i * len(head_AL): (i + 1) * len(head_AL)]
    table_q2_a_AL_prettify.append(s)

table_q2_a_AL_prettify
for i in range(15):
    df_home_run_AL_b.loc[i] = table_q2_a_AL_prettify[i]

# In[79]:


df_home_run_AL_b.to_csv('C:\BIA Sycn\BIA660\Question_2_b_AL.csv')

# In[81]:


al_data_b = pd.read_csv('C:\BIA Sycn\BIA660\Question_2_b_AL.csv')
al_mean_q2_b = al_data_b['HR'].mean()
print(al_mean_q2_b)

# In[80]:


##for NL
NL_bar = driver.find_element_by_css_selector(
    '#st_hitting-0 > fieldset:nth-child(2) > label:nth-child(6) > span:nth-child(1)')
NL_bar.click()
time.sleep(10)
hitting_splits_element = driver.find_element_by_id('st_hitting_hitting_splits')
splits_select = Select(hitting_splits_element)
splits_select.select_by_visible_text('First Inning')

# In[ ]:


time.sleep(10)
hitting_splits_element = driver.find_element_by_id('st_hitting_hitting_splits')
splits_select = Select(hitting_splits_element)
splits_select.select_by_visible_text('First Inning')

# In[84]:


data_div_NL = driver.find_element_by_id('datagrid')
data_html_NL = data_div_NL.get_attribute('innerHTML')
soup_NL = bs4.BeautifulSoup(data_html_NL, "html5lib")
head_NL = [t.text.replace("▼", "") for t in soup_NL.thead.find_all("th")]
df_home_run_NL_b = pd.DataFrame(columns=head_NL)

table_q2_a_NL = []
for t in soup_NL.tbody.find_all("tr"):
    for a in t.find_all("td"):
        table_q2_a_NL.append(a.text)

table_q2_a_NL_prettify = []
for i in range(int(len(table_q2_a_NL) / len(head_NL))):
    s = table_q2_a_NL[i * len(head_NL): (i + 1) * len(head_NL)]
    table_q2_a_NL_prettify.append(s)

for i in range(15):
    df_home_run_NL_b.loc[i] = table_q2_a_NL_prettify[i]

df_home_run_NL_b.to_csv('C:\BIA Sycn\BIA660\Question_2_b_NL.csv')

# In[86]:


nl_data_b = pd.read_csv('C:\BIA Sycn\BIA660\Question_2_b_NL.csv')
nl_mean_q2_b = nl_data_b['HR'].mean()

# In[88]:


if al_mean_q2_b >= nl_mean_q2_b:
    print("The league with greatest avg num of homeruns in the first inning:AL", al_mean_q2_b)
else:
    print("The league with greatest avg num of homeruns in the first inning:NL", nl_mean_q2_b)

# In[ ]:


# Question 3

