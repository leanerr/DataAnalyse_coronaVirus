#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import numpy as np
data = pd.read_excel('C:\\Users\\negin\\Downloads\\dataset\\iran_corona1.xlsx' , header = None ,
                     names= ['Date', 'New', 'N_sum', 'Death' , 'Death_sum' ] )
data.head()


# In[30]:


# فراخوانی کتابخانه های اولیه
import numpy
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd


# In[31]:


# آماده کردن دیتاست برای خوشه بندی 
data.drop('Date', axis=1, inplace=True)


# In[32]:


inertia_list=[]
for k in numpy.arange(1, 10):
    kmn= KMeans(n_clusters=k)
    kmn.fit(data.values)
    inertia_list.append(kmn.inertia_)
    
inertia_list


# In[33]:


# مشخص کردن تعداد خوشه های لازم
plt.plot(numpy.arange(1, 10), inertia_list, 'ro-')
plt.xlabel('number of clusters')
plt.ylabel('overlap')
plt.show()


# In[34]:


# انجام عملیات خوشه بندی
kmn = KMeans(n_clusters=3)
kmn.fit(data.values)
labels = kmn.predict(data.values)
labels


# In[35]:


# ترسیم نمودار براکندگی دو بعدی براساس مرگ روزانه و مبتلایان روزانه به تفکیک خوشه ها
xs = data.values[:,0]
ys = data.values[:,2]
plt.scatter(xs, ys, c=labels)
plt.legend(labels, loc='upper right')
plt.xlabel('new cases by day')
plt.ylabel('new death by day')
plt.show()


# In[36]:


# ترسیم گراف پراکندگی سه بعدی
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xs = data.values[:,0]
ys = data.values[:,1]
zs = data.values[:,2]
ax.scatter(xs, ys, zs, c=labels)
ax.legend(labels, loc= 'upper right')
ax.set_xlabel('A')
ax.set_ylabel('B')
ax.set_zlabel('C')
plt.show()


# In[46]:


columns = ['Cluster']
data2=pd.DataFrame(labels, index= None, columns=columns)
data2.head()

