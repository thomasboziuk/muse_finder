# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 21:48:00 2020

@author: Tom

This module defines the "muse finder" function set. Just a fun way to pick who
you should use as inspiration, based on the box office results on the day of
your birth.

"""
#dependencies
import requests
import re
from bs4 import BeautifulSoup
from dateutil import parser
import numpy as np
from time import sleep



#Will find the correct box office week for your birthday. Returns both the week, the name of the movie,
#and a URL for the movie
def getMovie(bday,base_url = 'https://www.boxofficemojo.com'):

    url = 'https://www.boxofficemojo.com/weekly/by-year/' + str(bday.year) + '/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    rows = soup.find_all('tr')
    weeks = []
    movies = []
    movieURLs = []
    for row in rows:
        dates = row.findChildren('td', class_ = re.compile('date_interval'))
        for date in dates[::2]:
            weeks.append(date.get_text())
        title = row.findChildren('td',class_ = re.compile('type-release'))
        for title in title:
            movies.append(title.a.get_text())
            movieURLs.append(title.a['href'])
    
    weekStarts = [parser.parse(date.split('-')[0]+ ' ' + str(bday.year)) for date in weeks]
    relevantWeekStart = np.argmax([(i-bday).days<0 for i in weekStarts])
    starUrl =  movieURLs[relevantWeekStart].split('?')[0]
    return ['Week of ' + weekStarts[relevantWeekStart].strftime('%b %d, %Y'), movies[relevantWeekStart], starUrl]


#Finds the 2 stars of a movie using a URL. This requires some additional navigation and parsing.
def getStars(starUrl, base_url = 'https://www.boxofficemojo.com'):
    
    page = requests.get(base_url + starUrl)
    soup = BeautifulSoup(page.content, 'html.parser')
    #for some reason, the cast and crew are on a different URL
    
    followLink = soup.find_all('a',class_ = re.compile('mojo-title-link'))
    for link in followLink:
        secondUrl = base_url + link['href'].split('?')[0] + 'credits/?ref_=bo_tt_tab#tabs'
    sleep(1)
    #sleep is just so you don't send two GET requests too quickly, to be polite
    
    page = requests.get(secondUrl)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    starRows = soup.find('table',id='principalCast').findChildren('tr')[1:3]
    stars = []
    for row in starRows:
        stars.append(row.a.get_text()[:-2])
    return stars

#When given a birthday, returns the 2 stars of the top-performing movie of that week.
#These are a person's muses... I guess?
def getMuse(month: str, day: int, year: int):
    bday = parser.parse(month + ' ' + str(day) + ' ' + str(year))
    return getStars(getMovie(bday)[2])

