#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier


# In[49]:

def ml(aa, bb):
    #دانیال این دوتا پایینی رو تعریف کن
    sex=bb
    age=aa
    def got_customer_age():
        #we should get age and sex here 
        np.array([age])
        
        customer_age=np.array([age])
        customer_sex=[]
        if sex =="male":
            customer_sex.append(1)
        else:
            customer_sex.append(0)
            
        customer_sex= np.array([customer_sex])
        return customer_age
        
    def got_customer_sex():
        customer_sex=[]
        if sex =="male":
            customer_sex.append(1)
        else:
            customer_sex.append(0)
            
        customer_sex= np.array([customer_sex])
        return customer_sex
    customer_age=got_customer_age()
    customer_sex=got_customer_sex()


    # In[50]:


    #import dataset

    titanic=pd.read_csv("extentions/titanic.csv")

    #recovery lost values

    titanic.isnull().sum()
    from sklearn.impute import SimpleImputer
    si=SimpleImputer(missing_values=np.nan,strategy="mean")
    age2=si.fit(titanic.Age.values.reshape(-1,1))
    age2=age2.transform(titanic.Age.values.reshape(-1,1))
    titanic["age2"]=age2
    titanic.age2


    # In[51]:


    from sklearn.neighbors import KNeighborsClassifier
    knn=KNeighborsClassifier()
    age2=titanic.age2.values.reshape(-1,1)
    sex2=titanic.Sex.values
    survived2=titanic.Survived.values.reshape(-1,1)
    titanic.Embarked.fillna("S",inplace=True)
    knn.fit(age2,survived2)
    predict_b_age=knn.predict((customer_age.reshape(1,-1)))


    # In[52]:


    #filters_sex=np.array([])
    filters_sex=[]
    for i in sex2:
        if i=="male":
            filters_sex.append(1)
        else:
            filters_sex.append(0)
    filters_sex=np.array([filters_sex])


    # In[53]:


    #predict
    knn.fit(filters_sex.reshape(-1,1),survived2)
    predict_b_sex=knn.predict(customer_sex.reshape(-1,1))


    # In[57]:


    mean_predict=np.mean([predict_b_sex,predict_b_age])
    if mean_predict==1:
        #show in the page "you are survived"
        return "fortnatly you survive"
    elif mean_predict==0:
        #show in the page you are not survived
        return "ufortnaltly you die"
    else:
        #show in the page "it is fifty fifty "
        return "it's fifty fifty"


    # In[ ]:
