import os
from flask import Flask
import requests
from bs4 import BeautifulSoup as bs4

app = Flask(__name__)

def get_fact():
    response = requests.get("http://unkno.com/")
    soup = bs4(response.content, "html.parser")
    fact = soup.find("div", {"id":"content"})
    return fact.getText().strip()

fact_data = {"siteurl": "https://hidden-journey-62459.herokuapp.com/", "input_text": get_fact()}

post_request = requests.post('https://hidden-journey-62459.herokuapp.com/', data = fact_data['input_text'])

if __name__=="__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host ='0.0.0.0', port=port)