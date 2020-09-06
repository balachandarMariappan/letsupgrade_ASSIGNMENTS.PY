#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(2,201):#to find prime number from 1 to 200
    flag=0
    for j in range(2,201):
        if(j<=i//2):
           if(i%j==0):
              flag=1
    if(flag==0):
           print(i,"is prime")
    


# In[ ]:




