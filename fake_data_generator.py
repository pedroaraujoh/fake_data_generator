#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# %pip install Faker Polars

# In[ ]:


from faker import Faker
from datetime import datetime, timezone
import random
import polars as pl
import os

# In[ ]:


HOME_PATH = os.getenv("HOME_PATH", "/home/user/")

# In[ ]:


fake = Faker('pt_BR')

now = datetime.now(timezone.utc)

# In[ ]:


len = random.randint(10, 20)

names = [fake.name() for _ in range(len)]
dates = [fake.date() for _ in range(len)]
states = [fake.state() for _ in range(len)]
colors = [fake.color_name() for _ in range(len)]
phrases = [fake.catch_phrase_verb() for _ in range(len)]
ages = [str(random.randint(1, 110)) for _ in range(len)]

timestamp = now.strftime("%Y-%m-%d %H:%M:%S %z")

# In[ ]:


df = pl.DataFrame({
    "name": names,
    "date": dates,
    "state": states,
    "color": colors,
    "phrase": phrases,
    "age": ages,
    "exec_timestamp": timestamp
})

# In[ ]:


date = now.strftime("%Y_%m_%d_%H_%M_%S")
file_name = f"fake_data_{date}.csv"
file_path = HOME_PATH + file_name

df.write_csv(file_path)
