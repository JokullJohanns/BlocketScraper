from flask import Flask
from flask import render_template
from bs4 import BeautifulSoup
import requests
import pickle 
app = Flask(__name__)

@app.route("/")
def index():
	items = getAds("")
	return render_template("index.html",
						   items=items)


def getAds(url):
	#r  = requests.get(url)
	#data = r.text
	#soup = BeautifulSoup(data, "html.parser")

	#pickle.dump( soup, open( "save.p", "wb" ) )

	soup = pickle.load( open( "BlocketRequest.p", "rb" ) )
	items = []

	for html_item in soup.select("#item_list > div"):
		item = {}
		item['title'] = getFirstOrDefault(html_item.select('.item_link.xiti_ad_heading'))
		item['image'] = getFirstOrDefault(html_item.select('.sprite_list_placeholder'))
		item['price'] = getFirstOrDefault(html_item.select('.li_detail_params.monthly_rent'))
		item['rooms'] = getFirstOrDefault(html_item.select('.li_detail_params.first.rooms'))
		item['address'] = getFirstOrDefault(html_item.select('.address'))
		items.append(item)
	return items

def getFirstOrDefault(l):
	if len(l) > 0:
		return l[0]
	else:
		return ""

items = getAds('https://www.blocket.se/bostad/uthyres/stockholm?f=p&f=c&f=b')

if __name__ == "__main__":
	app.run(debug=True)
