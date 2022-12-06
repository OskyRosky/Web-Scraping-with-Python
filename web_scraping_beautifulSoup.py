########################################################################################
# Web Scraping with BeautifulSoup
# https://www.youtube.com/watch?v=GlF1Lkjbp7E&ab_channel=JieJenn
########################################################################################

############################
#       Libraries          #
############################

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Python code to illustrate Sending mail with attachments
# from your Gmail account 
  
############################
#   Stablish a directory   #
############################


# Get the current working directory  : os.getcwd()
cwd = os.getcwd()
cwd

# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Let's set the directory 

path = 'C:\\Users\\oscar\\Desktop\\GitHub\\Python\\Projetcs\\P2'


# Change the current working directory
os.chdir(path)

# Let's check the new directory 

print("Current working directory: {0}".format(os.getcwd()))


############################
#         Scrapping        #
############################

headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

base_url = "https://www.coingecko.com/en"

tables = []

for i in range(1, 4):
    print('Processing page {0}'.format(i))
    params = {
        'page': i
    }
    response = requests.get(base_url, headers=headers, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables.append(pd.read_html(str(soup))[0])

master_table = pd.concat(tables)
master_table = master_table.loc[:, master_table.columns[1:-1]]
master_table.to_csv('Crypto_Data_Table.csv', index=False)
