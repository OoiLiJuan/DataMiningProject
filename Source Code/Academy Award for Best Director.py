Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> website_url = requests.get ('https://en.m.wikipedia.org/wiki/Academy_Award_for_Best_Director')
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup (website_url.text,'html.parser')
>>> print (soup.prettify())

>>> 
My_table=soup.find('table', class_='wikitable sortable')
>>> My_table

>>> director=[]
>>> films=[]
>>> for row in My_table.find_all('tr')[1:]:
    director_cell = row.find('td')
    director.append(director_cell.text)

>>> 
for row in My_table.find_all('i')[1:]:
    film_cell = row.find('a')
    films.append(film_cell.text)

>>> import pandas as pd
>>> directornominee= pd.DataFrame({'director': director})
>>> print(directornominee.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 460 entries, 0 to 459
Data columns (total 1 columns):
director    460 non-null object
dtypes: object(1)
memory usage: 3.7+ KB
None
>>> directornominee.to_csv('directornominee.csv')
>>> directorfilms= pd.DataFrame({'films': films})
>>> print(directorfilms.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 449 entries, 0 to 448
Data columns (total 1 columns):
films    449 non-null object
dtypes: object(1)
memory usage: 3.6+ KB
None
>>> directorfilms.to_csv('directorfilms.csv')
>>> 
