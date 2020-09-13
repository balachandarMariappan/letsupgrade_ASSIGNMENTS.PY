#!/usr/bin/env python
# coding: utf-8

# In[1]:


def good(lst):
    for num in (lst):

   # order of number
        order = len(str(num))
    
   # initialize sum
        sum = 0

        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            yield(num)
            


# In[2]:


lst=list(range(1,1000))


# In[3]:


print(list(good(lst)))


# In[ ]:





# In[ ]:




