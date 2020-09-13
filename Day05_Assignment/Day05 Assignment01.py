#!/usr/bin/env python
# coding: utf-8

# In[42]:


def checksublist(lst,sublist):
    correct,incorrect=0,0
       
    for i in sublist:
        if(all (x in sublist) for x in lst):
            correct+=1
        else:
            incorrect+=1
    if (correct>incorrect):
        print ("It's a Match") 
    else:
        print ("It's Gone") 

sublist=[1,1,5]
lst = [1,5,6,4,1,2,3,5] 

checksublist(lst,sublist)


# In[40]:


lst1=[1,5,6,5,1,2,3,6]


# In[41]:


checksublist(lst1,sublist)


# In[ ]:




