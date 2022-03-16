#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

password = random.randint(0,999999)
for i in range(3):
    parol = int(input('Enter a password: '))
    if parol == password:
         print('Welcome')
         break
    else:
        print('Incorrect,try again!')
        print('--------------------')

if parol != password:
    print ('3 incorrect tries ---- Locked out')
    print("Password is {}".format(parol))


# In[ ]:




