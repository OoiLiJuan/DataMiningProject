Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> import bs4
>>> r = requests.get ('https://www.imdb.com/list/ls095396246/?sort=list_order,asc&st_dt=&mode=detail&page=4')
>>> r.text

>>> from bs4 import BeautifulSoup
>>> 
soup = BeautifulSoup(r.text,'html.parser')
>>> # Select all the best picture nominee movies from at the web page
results = soup.find_all('div', attrs={'class':'lister-item mode-detail'})
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
RangeIndex: 58 entries, 0 to 57
Data columns (total 9 columns):
movie                 58 non-null object
year                  58 non-null object
genre                 58 non-null object
movie rating          58 non-null object
director and casts    58 non-null object
votes                 58 non-null int64
duration              58 non-null object
gross                 58 non-null object
detail                58 non-null object
dtypes: int64(1), object(8)
memory usage: 4.2+ KB
None
>>> # Export to csv 
movienominee.to_csv('best_picture4_nominee.csv')
>>> 
