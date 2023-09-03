#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[22]:


df=pd.read_csv(r'C:\Users\SK Laptop Town\Downloads\archive (3)\covid_vaccine_statewise.csv')
df


# 

# In[24]:


df[5:78]


# In[10]:


first_dose=df.groupby("State").sum()["First Dose Administered"]


# In[11]:


first_dose.head()


# In[12]:


second_dose=df.groupby("State").sum()["Second Dose Administered"]


# In[13]:


second_dose.head()


# In[14]:


male_vaccinated=df["Male(Individuals Vaccinated)"].sum()


# In[15]:


print(male_vaccinated)


# In[16]:


female_vaccinated=df["Female(Individuals Vaccinated)"].sum()
print(female_vaccinated)


# In[29]:


columns = ['Male (Doses Administered)','Female (Doses Administered)','18-44 Years(Individuals Vaccinated)','45-60 Years(Individuals Vaccinated)','60+ Years(Individuals Vaccinated)']
df[df[columns].notnull().all(1)]
 


# In[ ]:




