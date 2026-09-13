"""
Collect country information from ScrapeThisSite.

This module retrieves the country data from the website and prepares
the extracted information for storage in a database and subsequent
machine learning analysis.
"""

import re
import sqlite3

import requests
import bs4
import sklearn

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

cursor.execute("SELECT population, area FROM country_info;")
population_area = cursor.fetchall()

cursor.close()
connection.close()

x = []
y = []

for population, area in population_area:
    x.append([population])
    y.append(area)


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=1
)

model = sklearn.linear_model.LinearRegression()
model.fit(x_train, y_train)

answer = model.predict(x_test)
score = sklearn.metrics.r2_score(y_test, answer)
mae = sklearn.metrics.mean_absolute_error(y_test, answer)
root_error = sklearn.metrics.mean_squared_error(y_test, answer) ** 0.5

print(score)
print(mae)
print(root_error)
