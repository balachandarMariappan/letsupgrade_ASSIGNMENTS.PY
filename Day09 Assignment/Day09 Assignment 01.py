#!/usr/bin/env python
# coding: utf-8

# In[74]:


get_ipython().run_cell_magic('writefile', 'chandru1.py ', "'''\nthis is our module\n'''\ndef primenum(i):\n    '''this our program'''\n    if i <= 1:\n        return False\n    for j in range(2, i):\n        if i % j == 0:\n            return False\n    return True")


# In[75]:


get_ipython().system(' pylint')


# In[85]:


get_ipython().run_cell_magic('writefile', 'dear.py', 'import chandru1\nimport unittest\nclass hello(unittest.TestCase):\n      def test_primenumber(self):\n        a=3\n        result=chandru1.primenum(a)\n        self. assertTrue(result)\nif __name__=="__main__":\n    unittest.main()\n        ')


# In[86]:


get_ipython().system(' python dear.py')


# In[ ]:





# In[ ]:




