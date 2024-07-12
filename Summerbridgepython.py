#!/usr/bin/env python
# coding: utf-8

# In[ ]:


3 + 7

print("hello")
# In[ ]:


print("hello")


# In[ ]:


name = "Den"
age = 25


# In[ ]:


print(age)


# In[ ]:


# This is a comment it will not run
# You can echo values without using print in the notebook
name


# # Variables and Values

# In[ ]:


# variables can be used in calculations
print(age)
age = age + 3
print(age)


# In[ ]:


# Order of operations matters!
first = 1
second = first* 5
first = 2 

print (first)
print (second)


# In[ ]:


# Values have types. Types affect what you can do with them.
print(5-3)
#print("hello" - "h")


# In[ ]:


print(len("hello"))
#print(len(6))


# In[ ]:


# Add hashtag in front of code to disable it from running but keeps it on record. kernal tab and restart to rerun cells to retry. 


# In[ ]:


## Challenge
Explain what each operator does

print(5 // 3)

print(5 / 3)

print(5 % 3)


# In[ ]:


print(5 // 3)


# In[ ]:


print(5 / 3)


# In[ ]:


print(5 % 3)


# In[ ]:


print(7 // 3)


# In[ ]:


print(7 / 3)


# In[ ]:


# // - floor operator, / - division, % - remainder= this is good for keeping track 


# # Getting Help 

# In[ ]:


# Rounding Numbers is built in
round(3.14159, 2)


# In[ ]:


help(round)


# In[ ]:


round(3.14159, ndigits=2)


# In[ ]:


# All functions return a new value
rounded_pi = round(3.14159, 2)
print(rounded_pi)


# In[ ]:


# making titles and sections is changing the line to markdown and then starting the line with a hastag.


# In[ ]:


## Challenge

get_ipython().run_line_magic('pinfo', 'happen')

radiance=1.0

radiance=max(2.1,2.0+min(radiance,1.1*radiance-0.5))


# In[ ]:


radiance=1.0
radiance=max(2.1,2.0+min(radiance,1.1*radiance-0.5))


# In[ ]:


help(min)


# In[ ]:


help(max)


# In[ ]:


print(radiance)


# In[ ]:


# first thing radiance is equal to one. second thing (functions work inside out) 


# In[ ]:


# breakdown of operations
radiance = 1.0

min_arg_2 = 1.1 * radiance - 0.5
print("Min arg 2:", min_arg_2)

min_result = min(radiance, min_arg_2)
print("min result:", min_result)

radiance = max(2.1,2.0 + min_result)
print(radiance)


# # A Breif Interlude with Git

# In[ ]:




