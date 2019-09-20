#!/usr/bin/env python
# coding: utf-8

# In[8]:


from itertools import combinations
S, part = input().split()
for i in range(1,int(part)+1):
    for j in combinations(sorted(S),i):
            print(''.join(j))


# In[ ]:




