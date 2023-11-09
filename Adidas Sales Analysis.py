#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# In[3]:


var = pd.read_csv('Adidas Sales.csv')


# In[4]:


df = pd.DataFrame(var)


# In[5]:


df.head()


# In[6]:


df.info()


# In[8]:


df.dtypes


# In[10]:


df.isnull().sum()


# In[12]:


df.dropna()


# In[13]:


df1 = df.iloc[[1,2,3,4,5,6,7,8,9]]


# In[15]:


df1.head(10)


# In[16]:


df.head()


# In[20]:


df['Price per Unit'] = df['Price per Unit'].str.replace('$',"")
df['Units Sold']= df['Units Sold'].str.replace(',',"")
df['Total Sales']= df['Total Sales'].str.replace('$',"").str.replace(',','')
df['Operating Profit']= df['Operating Profit'].str.replace('$',"").str.replace(',',"")
df['Operating Margin']= df['Operating Margin'].str.replace('%',"")


# In[21]:


df.head()


# In[22]:


df['Price per Unit'] = df['Price per Unit'].astype('float64').astype('int64')
df['Units Sold']= df['Units Sold'].astype('int64')
df['Total Sales']= df['Total Sales'].astype('int64')
df['Operating Profit']= df['Operating Profit'].astype('int64')
df['Operating Margin']= df['Operating Margin'].astype('int64')


# In[23]:


df.head()


# In[24]:


df.loc[df['Units Sold'] >= 1000 , 'Units Segregation'] = 'High Units'
df.loc[df['Units Sold']< 1000 , 'Units Segregation'] = 'Medium Units'
df.loc[df['Units Sold'] < 500 , 'Units Segregation'] = 'Low Units'


# In[26]:


df['Units Segregation'].unique()


# In[25]:


df.head()


# In[27]:


df['Invoice Date'] = pd.to_datetime(df['Invoice Date'],format = "%d-%m-%Y")


# In[28]:


df['Month'] = df['Invoice Date'].dt.strftime('%B')


# In[29]:


df['Weekday'] = df['Invoice Date'].dt.strftime('%A')


# In[30]:


df.head()


# # Matplotlib

# In[32]:


df2 = df.groupby('Product').agg({'Units Sold':'sum','Total Sales':'sum','Operating Profit':'sum'}).reset_index()


# In[33]:


df2.head()


# In[34]:


plt.title('Productwise Sales',fontsize = 20)
plt.xlabel('Products',fontsize = 10)
plt.ylabel('Total Sales',fontsize = 10)
plt.bar(df2['Product'],df2['Total Sales'],label = 'Sales',edgecolor = 'Red',color = 'Blue',width = 0.4)
plt.legend()
plt.xticks(rotation = 40)
plt.show()


# In[37]:


plt.title('Productwise Sales',fontsize = 20)
plt.xlabel('Products',fontsize = 10)
plt.ylabel('Total Sales',fontsize = 10)
plt.bar(df2['Product'],df2['Total Sales'],label = 'Sales',edgecolor = 'Red',color = 'Blue',width = 0.4)
plt.bar(df2['Product'],df2['Operating Profit'],label = 'Profit',edgecolor = 'Red',color = 'yellow',width = 0.4)
plt.legend()
plt.xticks(rotation = 40)
plt.show()


# In[40]:


plt.title('Productwise Sales',fontsize = 20)
plt.xlabel('Products',fontsize = 10)
plt.ylabel('Total Sales',fontsize = 10)
plt.plot(df2['Product'],df2['Total Sales'],marker = "*")
plt.show()


# In[43]:


plt.title('Productwise Sales',fontsize = 20)
plt.xlabel('Products',fontsize = 10)
plt.ylabel('Total Sales',fontsize = 10)
plt.scatter(df2['Product'],df2['Total Sales'],marker = "*")
plt.show()


# In[51]:


plt.title('Productwise Sales',fontsize = 20)
plt.xlabel('Products',fontsize = 10)
plt.ylabel('Total Sales',fontsize = 10)
plt.hist(df2['Product'])
plt.xticks(rotation = 40)
plt.show()


# In[49]:


plt.pie(df2['Total Sales'],labels = df2['Product'],autopct = '%0.1f%%',radius = 0.9)
plt.show()


# # Seaborn 

# In[58]:


sns.lineplot(x = 'Product',y = 'Total Sales',data = df2,marker = '*')
plt.xticks(rotation = 40)


# In[55]:


sns.barplot(x = 'Product',y = 'Total Sales',data = df2,palette = 'YlGnBu')
plt.xticks(rotation = 40)


# In[60]:


sns.scatterplot(x = 'Product',y = 'Total Sales', data = df2,hue = 'Product')
plt.xticks(rotation = 40)


# In[62]:


sns.histplot(x = 'Total Sales',data = df,hue = 'Product',kde = True,bins = 10)


# In[88]:


sns.jointplot(x = 'Total Sales',y = 'Operating Profit', data = df2,kind = 'kde',shade = True)


# In[73]:


sns.pairplot(df2)


# In[74]:


df2.head()


# In[76]:


df2.drop(columns = ['Product'],inplace = True)


# In[77]:


df2.head()


# In[78]:


df2.corr()


# In[86]:


sns.heatmap(df2.corr(),annot = True, cmap = 'coolwarm')


# In[ ]:




