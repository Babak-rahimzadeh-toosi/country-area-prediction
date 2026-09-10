"""
Collect country information from ScrapeThisSite.

This module retrieves the country data from the website and prepares
the extracted information for storage in a database and subsequent
machine learning analysis.
"""

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


