import os
from flask import Flask
import requests
from bs4 import BeautifulSoup as bs4


response = requests.get("http://unkno.com/")
soup = bs4(response.content, "html.parser")
fact = soup.find("div", {"id":"content"})

print(fact.getText().strip())