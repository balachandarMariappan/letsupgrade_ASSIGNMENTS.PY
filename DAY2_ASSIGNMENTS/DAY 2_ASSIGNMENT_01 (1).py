#!/usr/bin/env python
# coding: utf-8

# # LIST WITH ITS METHODS

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[38]:


lst=[1,2.3,"HERO",4,8] #creating a list


# In[39]:


lst #executing the list


# In[40]:


lst.append(5) #invoking append() method


# In[41]:


lst # element '5' will be added at end


# In[42]:


lst.insert(1,5) #invoking insert() method


# In[43]:


lst # element '5' will be added in the index '1'


# In[44]:


lst.count(5) # invoking count() method to count the element '5'


# In[45]:


lst.pop(2)      #invoking pop() method to pop the element in the index '2' and it will be removed


# In[46]:


lst               # here see the element in the index '2'


# In[47]:


lst.remove(5) # invoking remove() method to remove the element '5' at very first  occurence


# In[48]:


lst


# In[49]:


lst.reverse() #invoking reverse() method to reverse list


# In[50]:


lst # here the elements in list are reversed


# In[51]:


lst1=[0,6,7] # just create a new list


# In[52]:


lst.extend(lst1) #invoking extend() method in order to join two list


# In[53]:


lst # list 'lst' is added at the end of list 'lst'


# # DICTIONARY   WITH  ITS METHODS

# In[157]:


DICT={"name":"Ram" ,  "gender":"Male" , "age" :20 }


# In[139]:


DICT.items() #invoking items() method to retrieve items


# In[140]:


DICT.keys() #invoking keys() method to retrieve keys


# In[141]:


DICT.get("name") #invoking get() method with key name to retrieve the respective value


# In[142]:


DICT.pop("name") #invoking pop() method to pop the value of specified key 


# In[143]:


DICT   # here see the popped key-value pair is removed


# In[144]:


DICT.update({"PWD":1452}) #invoking update() method


# In[145]:


DICT #the specified key-value pair is updated


# In[146]:


DICT.popitem() #invoking popitem() method to pop the last key-value pair


# In[147]:


DICT.values() #invoking values() method to get values in the dictionary


# # TUPLES WITH ITS METHODS

# In[158]:


TUP=(1,2,3,4,4,5,5,4,3)


# In[153]:


TUP


# In[155]:


TUP.count(4)#invoking count() method to count how many times the specified element is repeated in tuple


# In[156]:


TUP.index(2) #invoking index() method to find the index of specified element in tuple


# # SETS WITH METHOD

# In[211]:


SETS={1,2,3.4,5,5,5,"RAM"} #sets donot allow repeatation of elements in it


# In[212]:


SETS # here you can see there is no repeation of any element


# In[213]:


SETS1={1,2,5,7,8,9,10} #creating new sets


# In[214]:


SETS.intersection(SETS1) #invoking intersection() method to find common elements in both sets


# In[215]:


SETS.difference(SETS1)  #invoking difference() method to find elements only in SETS but not in SETS1 


# In[216]:


SETS.union(SETS1) #invoking union() method to combine elements in both sets


# In[217]:


SETS.discard(5) #invoking discard() method to remove  the specified element from the sets


# In[218]:


SETS #element '5' is removed


# In[219]:


SETS.pop() #invoking pop to remove the first element in sets


# In[222]:


SETS


# # STRING WITH ITS METHOD

# In[254]:


Chandru="HAI GUYS "


# In[255]:


Chandru.capitalize() #invoking capitalize() method to make only the letter of the string as capital and others as small


# In[256]:


Chandru #string is immutable


# In[257]:


Chandru1="HELLO HELLO WORLD"


# In[258]:


Chandru1.casefold() #invoking casefold() method to make all letters of the string as small


# In[259]:


Chandru1.count('HELLO') #invoking count() method to find how many times the specified word is occcured in the string


# In[260]:


Chandru1.endswith('D')


# In[266]:


Chandru2="ABCdefg"


# In[267]:


Chandru2.swapcase() #invoking swapcase() method in string to convert uppercase into lowercase and viceversa 


# # DAY2 ASSIGNMENT COMPLETED

# In[ ]:




