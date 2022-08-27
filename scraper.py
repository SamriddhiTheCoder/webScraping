import time
import csv
from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

headers = ["name", "distance", "mass", "radius"] 
star_data = []

def scrape(): 
    page = requests.get(START_URL)
    soup = BeautifulSoup(page.content,"html.parser") 
    temp_list = []
    time.sleep(3)
    tr_tag = soup.find_all("tr")
    for tr in tr_tag:
        td = tr.find_all("td")
        row = [i.text.rstrip()for i in td]
        temp_list.append(row)

    star_names = []
    distances  = []
    masses = [] 
    radiuses = []
    for i in range(1, len(temp_list)):
        star_names.append(temp_list[i][1])
    for i in range(1, len(temp_list)):
        distances.append(temp_list[i][3])
    for i in range(1, len(temp_list)):
        masses.append(temp_list[i][5])
    for i in range(1, len(temp_list)):
        radiuses.append(temp_list[i][6])
    #list rows 1, 3, 5, 6

    df = pd.DataFrame(star_data)
    df.insert(0, 'Name', star_names)  
    df.insert(1, 'Distance', distances)  
    df.insert(2, 'Mass', masses) 
    df.insert(3, 'Radius', radiuses) 
    df.to_csv("data.csv")

scrape()

#with open("data.csv", "w") as f: 
    #csvwriter = csv.writer(f)
    #csvwriter.writerow(headers) 
    #csvwriter.writerows(star_data)

