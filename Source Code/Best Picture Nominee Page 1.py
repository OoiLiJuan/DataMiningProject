Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> import bs4
>>> r = requests.get ('https://www.imdb.com/list/ls095396246/?sort=list_order,asc&st_dt=&mode=detail&page1')
>>> r.text

>>> print (r.text[0:500])




<!DOCTYPE html>
<html
    xmlns:og="http://ogp.me/ns#"
    xmlns:fb="http://www.facebook.com/2008/fbml">
    <head>
         
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <meta name="apple-itunes-app" content="app-id=342792525, app-argument=imdb:///list/ls095396246?src=mdot">



        <script type="text/javascript">var IMDbTimer={starttime: new Date().getTime(),pt:'java'};</script>

<script>
    if (typeof uet == 'function') {
      uet(
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(r.text,'html.parser')

>>> # Select all the best picture nominee movies from at the web page
results = soup.find_all('div', attrs={'class':'lister-item mode-detail'})

>>> len(results)
100
>>> firstresult = results [0]
>>> firstresult

>>> # Extract movie title
firstresult.h3.a.text
'Green Book'
>>> # Extract year of movie's release
firstresult.h3.find('span',class_ = 'lister-item-year text-muted unbold').text
'(2018)'
>>> # Extract movie genre
firstresult.find('span',class_ = 'genre').text.strip(' \n')

'Biography, Comedy, Drama'
>>> # Extract the movie rating
firstresult.find('span',class_ = 'ipl-rating-star__rating').text
'8.2'
>>> # Extract director and casts
firstresult.find_all('p', attrs={'class':'text-muted text-small'})[1].text.strip(' \n')
'Director:\nPeter Farrelly\n| \n    Stars:\nViggo Mortensen, \nMahershala Ali, \nLinda Cardellini, \nSebastian Maniscalco'
>>> # Extract the Metascore
int (firstresult.find('span', class_ = 'metascore favorable').text)

69
>>> # Extract the number of votes
int (firstresult.find('span',attrs = {'name':'nv'})['data-value'])
243148
>>> # Extract the movie duration
firstresult.find('span',class_ = 'runtime').text
'130 min'
>>> # Extract the movie gross
firstresult.find_all('p', class_ = 'text-muted text-small')[2].text[25:34]
'$85.08M\n'
>>> #Extract the movie details
firstresult.find('p', attrs={'class':''}).text.strip(' \n')
'A working-class Italian-American bouncer becomes the driver of an African-American classical pianist on a tour of venues through the 1960s American South.'
>>> # Lists to store the scraped data in
titles = []
>>> years = []
>>> genres = []
>>> directorcasts =[]
>>> movieratings = []
>>> votes = []
>>> durations = []
>>> grosss = []
>>> details = []

>>> for imdbnominee in results:
# Extract if the movie has movie rating, votes, movie duration, gross, movie details
	if imdbnominee.find('div', 'p', class_ = 'ipl-rating-star small' or 'text-muted text-small ' or 'text-muted ' or 'sort-num_votes-visible') is not None:
# Movie Title
		title = imdbnominee.h3.a.text
		titles.append (title)
# Year of movie's release
		year = imdbnominee.h3.find('span',class_ = 'lister-item-year text-muted unbold').text
		years.append (year)
# Movie Genre
		genre = imdbnominee.find('span',class_ = 'genre').text.strip(' \n')
		genres.append (genre)
# Movie Rating
		movierating = imdbnominee.find('span',class_ = 'ipl-rating-star__rating').text
		movieratings.append (movierating)
# Director and Casts
		directorcast = imdbnominee.find_all('p', attrs={'class':'text-muted text-small'})[1].text.strip(' \n')
		directorcasts.append (directorcast)
# The number of votes
		vote = int (imdbnominee.find('span',attrs = {'name':'nv'})['data-value'])
		votes.append (vote)
# Movie duration
		duration = imdbnominee.find('span',class_ = 'runtime').text
		durations.append(duration)
# Gross
		gross = imdbnominee.find_all('p', class_ = 'text-muted text-small')[2].text[25:34]
		grosss.append(gross)
# Movie Details
		detail = imdbnominee.find('p', attrs={'class':''}).text.strip(' \n')
		details.append(detail)


>>> import pandas as pd
>>> movienominee = pd.DataFrame({'movie': titles,'year': years,'genre':genres,'movie rating': movieratings,'director and casts': directorcasts,'votes': votes,'duration':durations,'gross':grosss, 'detail': details})
>>> print(movienominee.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 99 entries, 0 to 98
Data columns (total 9 columns):
movie                 99 non-null object
year                  99 non-null object
genre                 99 non-null object
movie rating          99 non-null object
director and casts    99 non-null object
votes                 99 non-null int64
duration              99 non-null object
gross                 99 non-null object
detail                99 non-null object
dtypes: int64(1), object(8)
memory usage: 7.1+ KB
None
>>> movienominee.head()
               movie  ...                                             detail
0         Green Book  ...  A working-class Italian-American bouncer becom...
1  Bohemian Rhapsody  ...  The story of the legendary British rock band Q...
2               Roma  ...  A year in the life of a middle-class family's ...
3      Black Panther  ...  T'Challa, heir to the hidden but advanced king...
4      The Favourite  ...  In early 18th century England, a frail Queen A...

[5 rows x 9 columns]
>>> # Export to csv 
movienominee.to_csv('best_picture1_nominee.csv')
>>> 
