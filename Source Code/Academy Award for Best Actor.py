Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> website_url = requests.get ('https://en.m.wikipedia.org/wiki/Academy_Award_for_Best_Actor')
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup (website_url.text,'html.parser')
>>> print (soup.prettify())

>>> My_table=soup.find('table', class_='wikitable sortable')
>>> My_table


>>> actor=[]
>>> films=[]
>>> for row in My_table.find_all('tr')[1:]:
    actor_cell = row.find_all('td')
    actor.append(actor_cell[0].a.text)

    
>>> for row in My_table.find_all('i')[1:]:
    film_cell = row.find('a')
    films.append(film_cell.text)

    
>>> import pandas as pd
>>> actornominee= pd.DataFrame({'actor': actor})
>>> print(actornominee.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 447 entries, 0 to 446
Data columns (total 1 columns):
actor    447 non-null object
dtypes: object(1)
memory usage: 3.6+ KB
None
>>> actornominee.to_csv('actornominee.csv')
>>> actorfilms= pd.DataFrame({'films': films})
>>> print(actorfilms.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 445 entries, 0 to 444
Data columns (total 1 columns):
films    445 non-null object
dtypes: object(1)
memory usage: 3.6+ KB
None
>>> actorfilms.to_csv('actorfilms.csv')
>>> 
