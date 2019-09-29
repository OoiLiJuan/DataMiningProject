Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> import bs4
>>> r = requests.get ('https://www.imdb.com/search/title/?count=100&groups=oscar_best_picture_winners&sort=year,desc&ref_=nv_ch_osc')
>>> r.text

>>> print (r.text[0:500])



<!DOCTYPE html>
<html
    xmlns:og="http://ogp.me/ns#"
    xmlns:fb="http://www.facebook.com/2008/fbml">
    <head>
         
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <meta name="apple-itunes-app" content="app-id=342792525, app-argument=imdb:///?src=mdot">



        <script type="text/javascript">var IMDbTimer={starttime: new Date().getTime(),pt:'java'};</script>

<script>
    if (typeof uet == 'function') {
      uet("bb", "LoadTitle"
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(r.text,'html.parser')
>>> # Select all the movies from at the web page
results = soup.find_all('div', attrs={'class':'lister-item mode-advanced'})

>>> len(results)
92
>>> winningresult = results [0]
>>> winningresult

>>> # Extract movie title
winningresult.h3.a.text
'Green Book'
>>> 
# Extract year of movie's release
winningresult.h3.find('span',class_ = 'lister-item-year text-muted unbold').text

'(2018)'
>>> # Extract movie genre
winningresult.find('span',class_ = 'genre').text.strip(' \n')

'Biography, Comedy, Drama'
>>> # Extract the movie rating
float(winningresult.strong.text)

8.2
>>> # Extract director and casts
winningresult.find('p', attrs={'class':''}).text.strip(' \n')
'Director:\nPeter Farrelly\n| \n    Stars:\nViggo Mortensen, \nMahershala Ali, \nLinda Cardellini, \nSebastian Maniscalco'
>>> # Extract the Metascore
int (winningresult.find('span', class_ = 'metascore favorable').text)
69
>>> # Extract the number of votes
int (winningresult.find('span',attrs = {'name':'nv'})['data-value'])
243182
>>> # Extract the movie duration
winningresult.find('span',class_ = 'runtime').text
'130 min'
>>> # Extract the movie gross
winningresult.find('p', class_ = 'sort-num_votes-visible').text [25:34]
'$85.08M\n'
>>> 
#Extract the movie details
winningresult.find_all('p', class_ = 'text-muted')[1].text.strip(' \n')
'A working-class Italian-American bouncer becomes the driver of an African-American classical pianist on a tour of venues through the 1960s American South.'
>>> # Lists to store the scraped data in
titles = []
>>> years = []
>>> genres = []
>>> directorcasts =[]
>>> movieratings = []
>>> metascores = []
>>> votes = []
>>> durations = []
>>> grosss = []
>>> # Extract data from each movie
for imdb in results:
# Extract if the movie has metascore
	if imdb.find('div', class_ = 'ratings-metascore') is not None:
# Movie Title
		title = imdb.h3.a.text
		titles.append (title)
# Year of movie's release
		year = imdb.h3.find('span',class_ = 'lister-item-year text-muted unbold').text
		years.append (year)
# Movie Genre
		genre = imdb.find('span',class_ = 'genre').text.strip(' \n')
		genres.append (genre)
# Movie Rating
		movierating = float(imdb.strong.text)
		movieratings.append (movierating)
# Director and Casts
		directorcast = imdb.find('p', attrs={'class':''}).text.strip(' \n')
		directorcasts.append (directorcast)
# Movie metascore
		metascore = int (imdb.find('span', class_ = 'metascore favorable').text)
		metascores.append (metascore)
# The number of votes
		vote = int (imdb.find('span',attrs = {'name':'nv'})['data-value'])
		votes.append (vote)
# Movie duration
		duration = imdb.find('span',class_ = 'runtime').text
		durations.append(duration)
# Gross
		gross = imdb.find('p', class_ = 'sort-num_votes-visible').text [25:34]
		grosss.append(gross)

>>> import pandas as pd
>>> moviewinning = pd.DataFrame({'movie': titles,'year': years,'genre':genres,'movie rating': movieratings,'director and casts': directorcasts,'metascore':metascores,'votes': votes,'duration':durations,'gross':grosss})
>>> print(moviewinning.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 71 entries, 0 to 70
Data columns (total 9 columns):
movie                 71 non-null object
year                  71 non-null object
genre                 71 non-null object
movie rating          71 non-null float64
director and casts    71 non-null object
metascore             71 non-null int64
votes                 71 non-null int64
duration              71 non-null object
gross                 71 non-null object
dtypes: float64(1), int64(2), object(6)
memory usage: 5.1+ KB
None
>>> moviewinning.head()
                                             movie  ...      gross
0                                       Green Book  ...  $85.08M\n
1                               The Shape of Water  ...  $63.86M\n
2                                        Moonlight  ...  $27.85M\n
3                                        Spotlight  ...  $45.06M\n
4  Birdman or (The Unexpected Virtue of Ignorance)  ...  $42.34M\n

[5 rows x 9 columns]
>>> moviewinning['year'].unique()
array(['(2018)', '(2017)', '(I) (2016)', '(I) (2015)', '(2014)', '(2013)',
       '(2012)', '(I) (2011)', '(2010)', '(2008)', '(2007)', '(2006)',
       '(2004)', '(I) (2004)', '(2003)', '(2002)', '(2001)', '(2000)',
       '(1999)', '(1998)', '(1997)', '(1996)', '(1995)', '(1994)',
       '(1993)', '(1992)', '(1991)', '(1990)', '(1989)', '(1988)',
       '(1987)', '(1986)', '(1985)', '(1984)', '(1983)', '(1982)',
       '(1981)', '(1980)', '(1979)', '(1978)', '(1977)', '(1976)',
       '(1975)', '(1974)', '(1973)', '(1972)', '(1971)', '(1970)',
       '(1969)', '(1968)', '(1967)', '(1966)', '(1965)', '(1964)',
       '(1963)', '(1962)', '(1961)', '(1960)', '(1959)', '(1957)',
       '(1954)', '(1953)', '(1951)', '(1950)', '(1946)', '(1942)',
       '(1939)', '(1935)', '(1934)', '(1930)'], dtype=object)
>>> moviewinning.loc[:, 'year'] = moviewinning['year'].str[-5:-1].astype(int)
>>> moviewinning['year'].head(3)
0    2018
1    2017
2    2016
Name: year, dtype: int32
>>> # Check the min and max value of movie rating and metascore
moviewinning.describe().loc[['min', 'max'], ['movie rating', 'metascore']]
     movie rating  metascore
min           6.5       63.0
max           9.2      100.0
>>> # Export to csv 
moviewinning.to_csv('movie_winning.csv')

>>> 
