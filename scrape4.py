# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:36:52 2020

@author: Shivani
"""
import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

session = requests.Session()
html = session.get("https://www.finder.com/in/netflix-movies")
soup=bs(html.content, "html.parser")

table=soup.find("table", attrs={"class":"luna-table luna-table--responsiveList ts-table"})


        # get the table headers
headers = []
for th in table.find("tr").find_all("th"):
    headers.append(th.text.strip())
print(headers)   

 # get all the rows of the table
rows = []
for tr in table.find_all("tr")[1:]:
    cells = []
    # grab all td tags in this table row
    tds = tr.find_all("td")
    if len(tds) == 0:
        # if no td tags, search for th tags
        # can be found especially in wikipedia tables below the table
        ths = tr.find_all("th")
        for th in ths:
            cells.append(th.text.strip())
    else:
       # use regular td tags
       for td in tds:
            cells.append(td.text.strip())
    rows.append(cells)
print(rows)
        # save table as csv file
table_name = f"Netflix"
print(f"[+] Saving {table_name}")
#save_as_csv(table_name, headers, rows)
pd.DataFrame(rows, columns=headers).to_csv(f"{table_name}.csv")