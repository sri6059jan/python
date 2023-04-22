#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install numpy


# # Min function

# In[67]:


L1=[1,2,3,4,5,6,7,0]

min_number=L1[0]

for i in range (0,len(L1),):
    if L1[i]<min_number:
     min_number =L1[i]   
else:
    print(min_number)
    


# # Maximum fun

# In[68]:


L1=[1,92,3,44,5,96,7]

max_number=L1[0]

for i in range(0,len(L1)):
    if L1[i]>max_number:
       max_number=L1[i]   
print(max_number)


# # Reverse

# In[6]:


L1=[1,2,3,4,5,6,7,8]
for i in range(len(L1),0-1,-1):
   print(i,end='')


# # Even and odd sepration

# In[7]:


L1=[1,2,3,4,5,6,7,8]
leven=[]
lodd=[]
for i in range(0,len(L1)):
    if L1[i]%2==0:
      leven.append(L1[i])
    else:
      lodd.append(L1[i])
print(leven)
print(lodd)


# In[8]:


print(leven+lodd)


# # update list without using update

# In[9]:


l=[1,2,3,4,5,6,7,8]
for i in range(0,len(l),):
    if l[i]%2==0:
      l[i]=10
print(l)
        

        

    


# # remove certain element  using for loop

# In[37]:


li=[1,2,3,4,5,6,7,8]
s=int(input())
for i in range(0,len(li)):
    if i ==s:
     li.remove(s)
print(li)
        
    


# In[55]:


l1=[1,2,3,4,5,6,7,8]
lremain=[]
for i in range(0,len(l1)):
    if i%2==0:
        lremain.append(l1[i])
print(lremain)
     
    


# In[61]:


l1=[1,2,3,4,5,6,7,8]
for i in range(0,len(l1)):
    if l1[i]%2==0:
        l1[i]=10
print(l1)


# In[ ]:




