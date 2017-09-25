'''
Noam Hiltzik 
09/06/2017
Copyright Hiltzik Data Laboratories

First Attempt at Scraping with BeautifulSoup

Test script using expedia.com for flights
from JFK to ORD roundtrip 
9/15 - 10/2
1 adult
-----------------------------------------------------
Dependencies:
bs4- Beautiful Soup
requests - pulling url information


-----------------------------------------------------
Variables
myUrl (str)
uClient (http.client.HTTPResponse)
'''

#imports
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd 
import numpy as py


#string containing url of search conducted on expedia
myUrl = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1311.R1.TR12.TRC2.A0.H0.Xray+.TRS0&_nkw=ray+ban+sunglasses&_sacat=0'
r = requests.get(myUrl)
pageSoup = soup(r.content, 'html.parser')
products = pageSoup.findAll("div", {"class":"mimg itmcd img"})
#print(len(products))
# product = products[7]
# pov = product.find("div", {"class": "prc"})
# print(len(pov.span.text))
# for product in products:
# 	pov = product.find("div", {"class": "prc"})
# 	print(pov.span)
for product in products:

    pov = product.find("div", {"class": "prc"})

    try:
    	currentPrice = pov.span.span.text
    except:
    	currentPrice = "N/A"

    print(currentPrice)

    try:
        previousPrice = pov.find("span", {"class": "stk-thr"}).text
    except:
    	previousPrice = "N/A"

    print(previousPrice)
    # if type(previousPrice) == 'NoneType':
    # 	previousPriceNone = "None"
    # 	print(previousPriceNone)
    # else:
    # 	print(previousPrice.text)
    try:
    	title = product.find("a", {"class": "vip"}).text
    except:
    	title = "N/A"
    print(title)
 #    try:
 #    	sold = product.find("div", {"class":"hotness-signal red"}).text
	# except:
	# 	sold = "N/A"

    # print(str(type(sold)))
    # print("i")
    # if str(type(sold)) == "<class 'bs4.element.Tag'>":

    # 	soldNone = "None"
    # 	print(soldNone)

    # else: 

    	# soldText = sold.text
    	# print(soldText)
    

   # print(sold)
   


# p = products[0]
# pov = p.find("div", {"class": "hotness-signal red"})
# print(type(pov))

# print(type("h"))