#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression


# In[18]:


from sklearn.datasets import load_boston 


# In[20]:


boston=load_boston()


# In[26]:


boston_df=pd.DataFrame(boston.data,columns=boston.feature_names)
boston_df['price']=boston.target
boston_df


# In[27]:


from sklearn.model_selection import train_test_split
x=boston.data
y=boston.target
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.3)


# In[30]:


reg = LinearRegression()
reg.fit(x_train,y_train)
y_pred= reg.predict(x_test)
plt.scatter(y_test,y_pred)
plt.xlabel('price')
plt.ylabel('predict price')


# In[31]:


from sklearn.metrics import mean_squared_error
mse =mean_squared_error(y_test,y_pred)
mse


# In[39]:


new_x = boston.data[:,[1,2]]
new_y = boston.target
new_x_train, new_x_test ,new_y_train, new_y_test = train_test_split(new_x, new_y, test_size = 0.3, random_state=42)
new_reg = LinearRegression()
new_reg.fit(new_x_train, new_y_train)
new_y_predict = new_reg.predict(new_x_test)
new_mse = mean_squared_error(new_y_test, new_y_predict)
new_mse

