#!/usr/bin/env python
# coding: utf-8

# In[81]:


import pandas as pd
import numpy as np
data = pd.read_excel('C:\\Users\\negin\\Downloads\\dataset\\iran_corona1.xlsx' , header = None ,
                     names= ['Date', 'New', 'N_sum', 'Death' , 'Death_sum' ] )
data.head()


# In[94]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn; seaborn.set()
data.pivot_table('New', ['Date']).plot()
plt.ylabel('total cases for iran');


# In[89]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn; seaborn.set()
data.pivot_table('Death', ['Date']).plot()
plt.ylabel('total cases for iran');


# In[35]:


sns.set()
N_sum = data['N_sum']
D_sum = data['Death_sum']
plt.plot(N_sum , D_sum)
plt.legend('Death', ncol=2, loc='upper left');


# In[96]:


sns.pairplot(data, size=7.5 )


# In[ ]:





# In[46]:


with sns.axes_style('white'):
    sns.jointplot("N_sum", "Death_sum", data=data, kind='hex')


# In[79]:


import seaborn as sns

sns.heatmap(pd.crosstab(data.New, [data.Death], values=data.Death, aggfunc='mean' ))


# In[80]:





# In[ ]:




