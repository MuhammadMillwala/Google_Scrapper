from flask import render_template,request
import requests, json
from forms import Search
from bs4 import BeautifulSoup

data=requests.get("https://trends.google.com/trends/explore?date=all&geo=PK&q=pakistani%20fashion").text
print(data)

