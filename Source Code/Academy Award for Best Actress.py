Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests

>>> website_url = requests.get ('https://en.m.wikipedia.org/wiki/Academy_Award_for_Best_Actress')
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup (website_url.text,'html.parser')
>>> print (soup.prettify())

>>> My_table=soup.find('table', class_='wikitable sortable')
>>> My_table

>>> actress=[]
>>> films=[]
>>> for row in My_table.find_all('tr')[1:]:
    actress_cell = row.find_all('td')
    actress.append(actress_cell[0].a.text)

    
>>> for row in My_table.find_all('i')[1:]:
    film_cell = row.find('a')
    films.append(film_cell.text)

    
>>> 
import pandas as pd
>>> 
>>> actressnominee= pd.DataFrame({'actress': actress})
>>> 
>>> print(actressnominee.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 451 entries, 0 to 450
Data columns (total 1 columns):
actress    451 non-null object
dtypes: object(1)
memory usage: 3.6+ KB
None
>>> actressnominee.to_csv('actressnominee.csv')
>>> actressfilms= pd.DataFrame({'films': films})
>>> print(actressfilms.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 451 entries, 0 to 450
Data columns (total 1 columns):
films    451 non-null object
dtypes: object(1)
memory usage: 3.6+ KB
None
>>> actressfilms.to_csv('actressfilms.csv')
>>> 
