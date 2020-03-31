import sys
import requests
from bs4 import BeautifulSoup
import xlrd
from tkinter.filedialog import askopenfilename
from xlwt import Workbook
from tkinter.filedialog import asksaveasfile

try:
    movie_list = []    #Create an empty list which will have list of movie names

    wb_write = Workbook() #Instantiate Excel module to write data into excel file
    sheet1 = wb_write.add_sheet('IMDB_Details')

    sheet1.write(0, 0, 'Title')
    sheet1.write(0, 1, 'IMDB Rating')
    sheet1.write(0, 2, 'MetaScore')
    sheet1.write(0, 3, 'Length')
    sheet1.write(0, 4, 'Year')
    sheet1.write(0, 5, 'Genre')
    sheet1.write(0, 6, 'Description')
    sheet1.write(0, 7, 'Release date')
    sheet1.write(0, 8, 'Rating')
    sheet1.write(0, 9, 'Director')
    sheet1.write(0, 10, 'Lead Cast')
    sheet1.write(0, 11, 'Country')
    sheet1.write(0, 12, 'Also Known As')
    sheet1.write(0, 13, 'Budget')
    sheet1.write(0, 14, 'Opening Weekend USA')
    sheet1.write(0, 15, 'Gross USA')
    sheet1.write(0, 16, 'Cumulative Worldwide Gross')
    sheet1.write(0, 17, 'Ratio')
    sheet1.write(0, 18, 'Taglines')


    filename = askopenfilename() #Ask User to open excel file to read data
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)

    counter = 1

    for i in range(sheet.nrows):
        if i == 0:
            continue
        movie_list.append(sheet.cell_value(i, 0))

    for movie in movie_list:
        page = requests.get('http://www.imdb.com/find?ref_=nv_sr_fn&q=' + movie + '&s=tt');
        soup1 = BeautifulSoup(page.content, 'html.parser')
        movieid = soup1.select(".findList tr a")[0].get('href')
        movielink = "http://www.imdb.com" + movieid
        mlinkpage = requests.get(movielink)
        soup2 = BeautifulSoup(mlinkpage.content, 'html.parser')
        titlenyear = soup2.select(".title_wrapper h1")[0].text
        movietitle = titlenyear[0:len(titlenyear) - 8]
        movieyear = titlenyear[len(titlenyear) - 6:len(titlenyear) - 2]
        movierating = soup2.select(".ratingValue span")[0].text
        metascore = soup2.select(".metacriticScore")
        metascore = metascore[0].text.strip() if metascore else None
        contentrating = soup2.find('meta',{'itemprop':'contentRating'})
        contentrating = contentrating['content'].strip() if contentrating else None
        movielength = soup2.select(".subtext time")[0].text.strip()
        genresndate = [i.text for i in soup2.select(".subtext a")]
        releasedate = genresndate[-1].strip()
        moviegenres = ""
        for i in soup2.find_all("div","txt-block"):
            if i.h4:
                if i.h4.text=="Budget:":moviebudget = i.h4.next_element.next_element.strip()
                if i.h4.text=="Opening Weekend USA:":movieopening = i.h4.next_element.next_element.strip()[:-1]
                if i.h4.text=="Gross USA:":movieusagross = i.h4.next_element.next_element.strip()[:-1]
                if i.h4.text=="Cumulative Worldwide Gross:":movieworldgross = i.h4.next_element.next_element.strip()[:-1]
                if i.h4.text=="Aspect Ratio:":movieratio = i.h4.next_element.next_element.strip()
                if i.h4.text=="Taglines:":movietaglines = i.h4.next_element.next_element.strip()
                if i.h4.text=="Also Known As:":moviealsoknown = i.h4.next_element.next_element.strip()
                if i.h4.text=="Country:":moviecountry = i.h4.next_sibling.next_element.text.strip()
        for x in range(len(genresndate) - 1):
            moviegenres = moviegenres + ',' + genresndate[x]
        moviegenres = moviegenres[1:]
        moviedesc = soup2.select(".summary_text")[0].text.strip()
        moviecast = [i.text for i in soup2.select(".credit_summary_item")]
        moviedirector = moviecast[0].split(":")[1:][0].split("\n")[1:][0]
        movieactors = moviecast[2].split(":")[1:][0].split("\n")[1:][0]

        print("Title: " + movietitle)
        print("IMDB Rating: " + movierating)
        if metascore: print("Metascore: " + metascore)
        print("Length: " + movielength)
        print("Year: " + movieyear)
        print("Genre: " + moviegenres)
        print("Description: " + moviedesc)
        print("Release date: " + releasedate)
        if contentrating: print("Rating: " + contentrating)
        print("Director: " + moviedirector)
        print("Lead Cast: " + movieactors)
        print("Country: " + moviecountry)
        print("Also Known As: " + moviealsoknown)
        print("Budget: " + moviebudget)
        print("Opening Weekend USA: " + movieopening)
        print("Gross USA: " + movieusagross)
        print("Cumulative Worldwide Gross: " + movieworldgross)
        print("Ratio: " + movieratio)
        print("Taglines: " + movietaglines)
        print("--------------------------------------------------------------------")

        #sheet1 = wb_write.add_sheet(movie)

        details = [movietitle, movierating, metascore, movielength, movieyear, moviegenres, moviedesc, releasedate
                  , contentrating, moviedirector, movieactors, moviecountry, moviealsoknown, moviebudget, movieopening
                  , movieusagross, movieworldgross, movieratio, movietaglines]


        for desc, i in zip(details,  range(len(details))):
            sheet1.write(counter, i, desc)

        counter = counter + 1

    f = asksaveasfile(mode='w', defaultextension=".csv")
    if f is not None:
        wb_write.save(f.name)
    f.close()

except Exception as e:
    print("Error is: {0}".format(repr(e)))