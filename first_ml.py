"""
Collect country information from ScrapeThisSite.

This module retrieves the country data from the website and prepares
the extracted information for storage in a database and subsequent
machine learning analysis.
"""
import sqlite3

import requests
import bs4
import re

response = requests.get("https://www.scrapethissite.com/pages/simple/", timeout=10)
data = response.text

structure = bs4.BeautifulSoup(data, "html.parser")
country_data = structure.find_all(class_="col-md-4 country")

countries: list = []


for ins in country_data:
    text = ins.get_text(strip=True)

    text = re.sub(r"\s+", " ", text)

    text = (
        text.replace("Capital:", ",")
        .replace("Population:", ",")
        .replace("Area (km2):", ",")
    ).split(",")

    countries.append(text)

connection = sqlite3.connect("country.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS country_info;")

cursor.execute("CREATE TABLE IF NOT EXISTS country_info("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "country TEXT UNIQUE NOT NULL,"
               "capital TEXT NOT NULL,"
               "population INTEGER NOT NULL,"
               "area INTEGER NOT NULL)")

for nations in countries:
    cursor.execute("INSERT INTO country_info(country, capital, population, area)"
                   " VALUES(?,?,?,?)", nations)

connection.commit()







