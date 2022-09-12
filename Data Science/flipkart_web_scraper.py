from dputils import scrape 

'''  
dputils is Digipodiums library that has scrape which helps in extracting data from website
Websites specially amazon blocks codes if it tries to access data from their websites multiple times
scrape has an inbuilt logic that helps intelligently acceses the data 
pretending to be accessing from a Browser befooling the website
'''

import pandas as pd

# step 1 - get the data as soup obj
# step 2 - create the setup dictionaries (most important)
# step 3 - pass the dictionaries into the extract_many() function
# step 4 - repeat step 1 to step 3 unitil data keeps coming
# step 5 - check and save data into a file


# Understanding the URL

URL_link = 'https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=7'


''' - before question mark is the address of main website after which we have parameters separated by &
    ['q=laptops', 'otracker=search', 'otracker1=search', 'marketplace=FLIPKART', 'as-show=on', 'as=off', 'page=7']

'''



# making our website link dynamic

###################### STEP 1 #########################


query = 'Laptop'
page = '1'
url = f'https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page}'

 
 ###################### STEP 2 #########################

# target dict, items dict , etc

t  = {'tag':'div', 'attrs':{'class':'_1YokD2 _3Mn1Gg'}}
rep_items =  {'tag':'div', 'attrs':{'class':'_1AtVbE col-12-12'}}
title = {'tag':'div', 'attrs':{'class':'_4rR01T'}}
price = {'tag':'div', 'attrs':{'class':'_30jeq3 _1_WHN1'}}
link = {'tag':'a', 'attrs':{'class':'_1fQZEK'}, 'output' : 'href'}




###################### STEP 3 #########################

'''data = scrape.extract_many(soup,
                           target =t,
                           items=rep_items,
                           title = title,
                           price=price,
                           link =link)
print(data)

'''




