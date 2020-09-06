#!/usr/bin/env python
# coding: utf-8

# In[ ]:


numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
zipped  # Holds an iterator object
type(zipped)
list(zipped)

