#!/usr/bin/env python
# coding: utf-8

# In[3]:


W = []
size= int(input("Enter the value = "))
for i in range(size):
    va= int(input("Enter the value = "))
    W.append(va)
a = max(W)
b= min(W)
print("Max value = ",a)
print("Min value = ", b)


# In[4]:


u = []
d = int(input("enter the value = "))
for i in range(d):
    val=int(input("enter the value= "))
    u.append(val)
print("Origanle List =",u)

max=u[0]
for i in range(d):
    if (u[i]>max):
        max=u[i]
print("Max value = ",max)

min=u[0]
for i in range(d):
    if (u[i]<min):
        min=u[i]
print("Min value = ",min)


# In[ ]:




