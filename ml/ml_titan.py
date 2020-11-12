#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier


# In[44]:


def got():
    #we should get age and sex here 
    customer_age=[32]
    customer_sex="male"
    return customer_age


# In[25]:


#import dataset
titanic=pd.read_csv("c://titanic.csv")
titanic.isnull().sum()
from sklearn.impute import SimpleImputer
si=SimpleImputer(missing_values=np.nan,strategy="mean")
age2=si.fit(titanic.Age.values.reshape(-1,1))
age2=age2.transform(titanic.Age.values.reshape(-1,1))
titanic["age2"]=age2
titanic.age2


# In[68]:


from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
age2=titanic.age2.values.reshape(-1,1)
sex2=titanic.Sex.values
survived2=titanic.Survived.values.reshape(-1,1)
titanic.Embarked.fillna("S",inplace=True)
customer_age=np.array([80])
knn.fit(age2,survived2)
predict_b_age=knn.predict((customer_age.reshape(1,-1)))


# In[99]:


#filters_sex=np.array([])
filters_sex=[]
for i in sex2:
    if i=="male":
        filters_sex.append(1)
    else:
        filters_sex.append(0)
filters_sex=np.array([filters_sex])


# In[104]:



knn.fit(filters_sex.reshape(-1,1),survived2)
customer_sex=np.array[1].reshape(-1,1)
predict_b_sex=knn.predict(np.array[1].reshape(-1,1))
predict_b_sex


# In[ ]:




