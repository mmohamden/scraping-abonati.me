from typing import Text
from numpy.lib.shape_base import tile
import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup
csv_file = open("26553,62656.csv", 'w', encoding='UTF-8', newline='')
writer = csv.writer(csv_file)
import numpy as np


pages = np.arange(1,26556, 1)
for i in pages:
    cookies = {
        '_ga': 'GA1.2.211277444.1625850430',
        '__gads': 'ID=261725dca91adb3c-22fbe0a968c90085:T=1625850431:RT=1625850431:S=ALNI_MYfQFIyvc5NcPohAvOssCfCmPqQUw',
        '_gid': 'GA1.2.272914211.1626128390',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }



    links =  'http://www.abonati.me/BUCURESTI-j10/BUCURESTI-l799/{}'.format(i + 1) 
    

    response = requests.get(links, headers=headers, cookies=cookies)
    print("parsing page", i+1)

    soup = BeautifulSoup(response.text, 'lxml')
    data = [] 

    table = soup.find_all('table')[0]

    rows = table.find_all('tr')[1:21]
    #print(rows)
    
    for row in rows:
        talent_dict = {}
        
        columns = row.find_all('td')
        Address = (columns[2].text.replace('\n', '').strip())

        name_Address = ''.join(Address).strip() if Address else None
        web = [a['href'] for a in columns[1].find_all('a', href=True,) if a.text.strip()]

        name_url = ''.join(web).replace("[", "").replace("]", "").strip() if web else None 
        
        talent_dict['name'] = name_Address
        talent_dict['website'] =name_url 
        writer.writerow(talent_dict.values())
        
csv_file.close()
   
            
            
            
            