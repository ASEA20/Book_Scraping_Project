import requests
from bs4 import BeautifulSoup
import csv
import time

url ='https://books.toscrape.com/catalogue/page-1.html'
response = requests.get(url)
soup=BeautifulSoup(response.text, 'html.parser')
books_details = soup.find_all('li',attrs={'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})



with open('Book.csv','w',newline="",encoding='utf-8') as f:
    fieldname = ['Book_Name','Book_Link','Book_Price','Book_Rating']
    dict = csv.DictWriter(f,fieldnames=fieldname)
    dict.writeheader()
    for i in range(len(books_details)):
        Book_Name=books_details[i].find_all('h3')[0].get_text()

        Book_Link='https://books.toscrape.com/catalogue/' + books_details[i].find_all('a')[0].get('href')
        
        Book_Price=books_details[i].find_all('p',attrs={'class':'price_color'})[0].get_text()
        Book_Rating=books_details[i].find_all('p',attrs={'class':'star-rating'})[0]['class'][1]
        

        dict.writerow({'Book_Name':Book_Name,'Book_Link':Book_Link,'Book_Price':Book_Price ,'Book_Rating':Book_Rating})