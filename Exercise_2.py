#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
import random

length = int(input("Enter length of password(8-13): "))
if (length>8) and (length<13):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = upper + lower + num + symbols

    temp = random.sample(all,length)

    password = "".join(temp)
    print(password)
else:
    print("The length is not in the range of 8-13")

