#!/usr/bin/env python
# coding: utf-8

# In[1]:


# prevalence
population = int(input("population: "))
existingcases = int(input("existingcases: "))
prevalence = existingcases / population
print(prevalence)
print(prevalence * 100000)


# In[2]:


# incidence
newcases = int(input("new cases"))
incidence = newcases / population
print(incidence)
print(incidence * 100000)


# In[3]:


# mortality rate
dead = int(input("number of those who died: "))
segment = int(input("number of people who had the disease: "))
mortalityrate = dead / segment
print(mortalityrate)
print(mortalityrate * 100000)

