#!/usr/bin/env python
# coding: utf-8

# In[15]:


# prevalence
population = int(input("population: "))
existingcases = int(input("existing cases: "))
prevalence = existingcases / population
print(prevalence)
print(prevalence * 10000)


# In[16]:


# incidence
newcases = int(input("new cases: "))
incidence = newcases / population
print(incidence)
print(incidence * 100000)


# In[13]:


# mortality rate
dead = int(input("number of those who died: "))
segment = int(input("number of people who had the disease: "))
mortalityrate = dead / segment
print(mortalityrate)
print(mortalityrate * 100000)


# In[18]:


# years of potential life lost
lifeexpectancy = 77
ages = [64, 74]
print(lifeexpectancy - ages[0])
print(lifeexpectancy - ages[1])


# In[19]:


lifelost = [13, 3]
yppl = sum(lifelost) / len(lifelost)
print(yppl)


# In[ ]:




