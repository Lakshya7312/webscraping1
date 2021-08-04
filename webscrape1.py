import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

html = requests.get(url, verify=False)
soup = BeautifulSoup(html.content, 'html.parser')
tables = soup.find_all('table')

names = []
distances = []
masses = []
radii = []

for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 1:
            name = cells[1].text
            names.append(name[:-1])

            distance = cells[3].text
            distances.append(distance[:-1])

            mass = cells[5].text
            masses.append(mass[:-1])

            radius = cells[5].text
            radii.append(radius[:-1])
dict = {'Proper Name': names, 'Distance': distances, 'Mass': masses, 'Radius': radii} 
     
df = pd.DataFrame(dict)
  
df.to_csv('result.csv')          
print("Process Completed")