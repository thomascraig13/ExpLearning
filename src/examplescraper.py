
#! NEEDED MODULES
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv


#! FILE TO SCRAPE TOP 5 MOVIES BY YEAR
class Scraper:

    def __init__(self):
        #! NEEDED VARIABLE(S)
        self.movies = []

    #! ACCESSES THE URL WITH THE YEAR GIVEN
    def page_parse(self,year):
        url = 'https://www.boxofficemojo.com/year/{0}/'.format(year)
        page = urlopen(url)			
        soup = BeautifulSoup(page, 'html.parser')

        rows = soup.findAll('tr')
        for row in rows[1:6]:
            td = row.findAll('td')
            
            ranking = td[0].text.strip()
            name = td[1].text.strip()
            releaseDate = td[8].text.strip()
            gross = int(td[5].text.strip().replace(',','').replace('$',''))
            total = int(td[7].text.strip().replace(',','').replace('$',''))

            #! ADDS TO MOVIE RANKING LIST
            self.movies.append([ranking,name,releaseDate,gross,total,year])

    #! CREATES FILE WITH STORED MOVIE RANKINGS
    def create_file(self):
        outfile = open('movies.csv','w',newline='')
        file = csv.writer(outfile,delimiter=',')
        file.writerow(['Ranking','Name','Release Date','Gross $', 'Total $','Year'])

        for row in self.movies:
            file.writerow(row)
