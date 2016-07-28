from flask import Flask
from flask import render_template
from bs4 import BeautifulSoup
import requests
import pickle 
app = Flask(__name__)
from Scraper import BlocketParser

@app.route("/")
def index():
	items = BlocketParser.getAds("")
	print(items)
	return render_template("index.html",
						   items=items)

if __name__ == "__main__":
	app.run(debug=True)
