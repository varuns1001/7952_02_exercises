#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime
df=pd.read_excel('SaleData.xlsx')


# 1. Find the least amount sale that was done for each item.

# In[18]:


df.groupby('Item')['Sale_amt'].min()


# 2. Compute the total sales for each year and region across all items

# In[19]:


def date_split(x):
    return x.year
df['order_year']=df['OrderDate'].apply(date_split)


# In[9]:


df.groupby(['order_year','Region'])['Sale_amt'].sum()


# 3. Create new column 'days_diff' with number of days difference between reference date passed and each order date

# In[16]:


def days_diff(x):
    return (x.date()-date_format).days

date_string=input("Enter a date")
date_format=datetime.strptime(date_string,'%B-%d-%Y').date()
df['diff']= df['OrderDate'].apply(days_diff)
df


# 4. Create a dataframe with two columns: 'manager', 'list_of_salesmen'. Column 'manager' will contain the
# unique managers present and column 'list_of_salesmen' will contain an array of all salesmen under
# each manager.

# In[3]:


new_df=pd.DataFrame()
new_df['manager']=df['Manager'].unique()


    


# In[4]:



def sale_man(x):
    return df[df['Manager']==x]['SalesMan'].unique()
new_df['list_of_salesman']=new_df['manager'].apply(sale_man)
new_df


# 5. For all regions find number of salesman and total sales. Return as a dataframe with three columns Region, salesmen_count and total_sales

# In[61]:



df.groupby('Region')['Units'].count()


# In[55]:


df['Region'].unique()


# In[56]:


region_salas=pd.DataFrame(index='Central East West'.split())


# In[58]:


region_salas['total_sales']=df.groupby('Region')['Units'].count()


# In[59]:


region_salas['salesmen_count']=df.groupby('Region')['SalesMan'].nunique()


# In[60]:


region_salas


# 6. Create a dataframe with total sales as percentage for each manager. Dataframe to contain manager
# and percent_sales
# 

# In[15]:


def perce_sales(x):
    return (x/2121)*100
persales=pd.DataFrame(index=df['Manager'].unique())
persales['percentsales']=(df.groupby('Manager')['Units'].sum()/2121)*100


# In[16]:


persales


# In[ ]:

#!/usr/bin/env python
# coding: utf-8

# In[90]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df=pd.read_csv('imdb.csv',error_bad_lines=False,escapechar='\\')
df2=pd.read_csv('movie_metadata.csv',escapechar='/')


# 7. Get the imdb rating for fifth movie of dataframe

# In[91]:


df.iloc[4]['imdbRating']


# 8. Return titles of movies with shortest and longest run time

# In[20]:



df[df['duration']==df['duration'].min()]['title']


# In[21]:



df[df['duration']==df['duration'].max()]['title']


# 9. Sort the data frame by in the order of when they where released and have higer ratings, Hint :
# release_date (earliest) and Imdb rating(highest to lowest)

# In[81]:



new_df=df.sort_values(by='year')
new_df


# In[87]:


l=new_df['year'].unique()
l


# In[94]:



df2=pd.DataFrame()
for i in l:    
    df2=df2.append(new_df[new_df['year']==i].sort_values(by='imdbRating',ascending=False))


# 1. Generate a report that tracks the various Genere combinations for each type year on year. The result
# data frame should contain type, Genere_combo, year, avg_rating, min_rating, max_rating,
# total_run_time_mins

# In[69]:


pr=pd.DataFrame()
pr=df.groupby(['year','type']).sum()


# In[70]:


pr['minrat']=df.groupby(['year','type'])['imdbRating'].min()
pr['maxrat']=df.groupby(['year','type'])['imdbRating'].max()
pr['avgrat']=df.groupby(['year','type'])['imdbRating'].mean()
pr['total_run_time']=df.groupby(['year','type'])['duration'].sum()



# In[71]:


list1=[]
for i in range(len(pr)):
    list=[]
    for j in range(9,37):
        if pr.iloc[i,j] > 0:
                    list=list+[pr.columns[j]]
    list1=list1+[list]

pr['genre_combo']=list1



# In[72]:


report1=pd.DataFrame(index=pr.index)
report1['genre_combo']=pr['genre_combo']
report1['minrat']=df.groupby(['year','type'])['imdbRating'].min()
report1['maxrat']=df.groupby(['year','type'])['imdbRating'].max()
report1['avgrat']=df.groupby(['year','type'])['imdbRating'].mean()
report1['total_run_time']=df.groupby(['year','type'])['duration'].sum()
report1


# 2. Is there a realation between the length of a movie title and the ratings ? Generate a report that captures
# the trend of the number of letters in movies titles over years. We expect a cross tab between the year of
# the video release and the quantile that length fall under. The results should contain year, min_length,
# max_length, num_videos_less_than25Percentile, num_videos_25_50Percentile ,
# num_videos_50_75Percentile, num_videos_greaterthan75Precentile

# In[74]:


fd=pd.DataFrame()
fd=df[['year','title']]
def find_length(x):
    return len(x)-7
fd['title_length']=fd['title'].apply(find_length)
max(fd['title_length'])


# In[75]:


fd['percentile']=(fd['title_length']/142)*100
fd


# In[76]:


fd[(fd['percentile']>75)].groupby('year')['title'].count()


# In[77]:


report2=pd.DataFrame()
report2['min_length']=fd.groupby('year')['title_length'].min()
report2['max_length']=fd.groupby('year')['title_length'].max()
report2['num_videos_less_than_25percentile']=fd[fd['percentile']<25].groupby('year')['title'].count()
report2['num_videos_25_50Percentile']=fd[(fd['percentile']>25)&(fd['percentile']<50)].groupby('year')['title'].count()
report2['num_videos_50_75Percentile']=fd[(fd['percentile']>50)&(fd['percentile']<75)].groupby('year')['title'].count()
report2['num_videos_greaterthan75Precentile']=fd[fd['percentile']>75].groupby('year')['title'].count()

report2


# In[78]:


def find_quantile(x):
    if x < 25:
        return 'first quantile'
    if x>25 and x<50:
        return 'second quantile'
    if x>50 and x<75:
        return 'third quantile'
    if x>75:
        return 'fourth quantile'
    
fd['quantile']=fd['percentile'].apply(find_quantile)
fd


# In[79]:


pd.crosstab(fd['year'],fd['quantile'],margins=False)


# 5. Bucket the movies into deciles using the duration. Generate the report that tracks various features like
# nomiations, wins, count, top 3 geners in each decile.

# In[81]:


df['decile_bins']=pd.qcut(df['duration'],10)
df


# In[82]:


new_df=pd.DataFrame()
new_df['nominations_count']=df.groupby('decile_bins')['nrOfNominations'].sum()
new_df['wins_count']=df.groupby('decile_bins')['nrOfWins'].sum()
new_df['count_numbers']=df.groupby('decile_bins')['tid'].count()



# In[83]:


fd=df.groupby('decile_bins').sum()
list2=[]
for i in range(len(fd)):
    list1=[]
    t=[]
    for j in range(10,38):
        list1=list1 + [fd.iloc[i,j]]
    arr=np.array(list1)
    l=np.argsort(arr)
    l=l[-3:]
    for i in range(len(l)):
        l[i]=l[i]+10
        t=t+[fd.columns[l[i]]]
    list2=list2+[t]
list2
new_df['popular_genre']=list2
new_df


# In[84]:


fd.columns.to_list()[10:]


# In[85]:


fd.columns.to_list()[-3:]


# In[88]:


list=[]
for j in range(10,38):
    list=list + [fd.iloc[0,j]]
arr=np.array(list)
l=np.argsort(arr)
l=l[-3:]
l
t=[]
t=t+[fd.columns[l[0]]]


# In[87]:


df.set_index('title',inplace=True)
df


# 6. Using the movie metadata set and the imdb data set come up with finidings (slice and dice the data to
# identify insights) and also create charts whereever possible.

# In[180]:


df['imdbRating'].hist()


# In[185]:


x=np.linspace(0,5,11)
y=x**2
y
x


# In[11]:


plt.subplot(2,1,1)
df['imdbRating'].plot(kind='hist',bins=100)
plt.xlabel('ratings from imdb dataset')

plt.subplot(2,1,2)

df2['imdb_score'].plot(kind='hist',bins=100)
plt.xlabel('ratings from movie dataset')


# In[12]:



df.plot.density()

df2.plot.density()


# In[21]:


df.plot.hexbin(x='year',y='imdbRating',gridsize=20,cmap='Oranges')

df2.plot.hexbin(x='title_year',y='imdb_score',gridsize=20,cmap='Oranges')


# In[23]:


df.head(50).plot.bar(stacked=True)


df2.head(50).plot.bar(stacked=True)


# In[61]:


df.plot.hexbin(x='duration',y='imdbRating',gridsize=20,cmap='Oranges')

df.plot.hexbin(x='year',y='duration',gridsize=20,cmap='Oranges')


# In[40]:


fd=pd.DataFrame()
fd=df[['year','title','imdbRating']]
def find_length(x):
    return len(x)-7
fd['title_length']=fd['title'].apply(find_length)


fd1=pd.DataFrame()
fd1=df2[['title_year','movie_title','imdb_score']]
def find_length1(x):
    return len(x)-1
fd1['title_length']=fd1['movie_title'].apply(find_length1)


# In[42]:


fd.plot.hexbin(x='title_length',y='imdbRating',gridsize=20,cmap='Oranges')


# In[60]:


fd1.plot.hexbin(x='title_length',y='imdb_score',gridsize=(20,20),cmap='Oranges')


# In[48]:


fd1.plot.line(x='title_length',y='imdb_score')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

df=pd.read_csv('diamonds.csv')
df.info()


# 11. Count the duplicate rows of diamonds DataFrame.

# In[58]:


df[df.duplicated()].count()


# 12. Drop rows in case of missing values in carat and cut columns.

# In[59]:


df.dropna(subset=['carat','cut'])


# 13. Subset the dataframe with only numeric columns.

# In[60]:


numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

df.select_dtypes(include=numerics)


# 14. Compute volume as (xyz) when depth is greater than 60. In case of depth less than 60 default volume to
# 8.

# In[3]:


df.loc[df[df['z']=='None']['z'].index,'z']=0
df['zfloat']=df['z'].astype(float)
tdf=df
def volume():
    
        tdf['volume']=(tdf['x'])*(tdf['y'])*tdf['zfloat']
        return tdf
volume()
tdf.loc[tdf[tdf['depth']<60]['depth'].index,'volume']=8
tdf


# 15. Impute missing price values with mean.

# In[5]:


df['price'].fillna(value=df['price'].mean(),inplace=True)
df['price']


# In[11]:


a=pd.qcut(df['volume'],q=4)
a


# Bonus Question
# 3. In diamonds data set Using the volumne calculated above, create bins that have equal population within
# them. Generate a report that contains cross tab between bins and cut. Represent the number under
# each cell as a percentage of total.

# In[12]:


pd.crosstab(a,df['cut'],margins=False)


# In[ ]:








