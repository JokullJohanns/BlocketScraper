#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import pickle 
import cssutils
import re

class BlocketParser:

	def __init__(self):
		pass

	@staticmethod
	def getFirstOrDefault(l):
	    if len(l) > 0:
	        return l[0]
	    else:
	        return None

	@staticmethod
	def getImage(tag):
	    if tag == None:
	        return None
	    else:
	        style = cssutils.parseStyle(tag['style'])
	        url = style['background-image']
	        url = url.replace('url(', '').replace(')', '')
	        return url

	@staticmethod
	def getRoomCount(tag):
	    if tag == None:
	        return None
	    else:
	        roomCount = re.sub("[^0-9,]", "", tag.text)
	        roomCount = float(re.sub("[,]", ".", roomCount))
	        return roomCount

	def getPrice(tag):
	    if tag == None:
	        return None
	    else:
	        priceText = tag.text
	        return re.sub("[^0-9]", "", priceText)
	
	@staticmethod    
	def getAddress(tag):
	    if tag == None:
	        return ""
	    else:
	        addressString = tag.text.strip()
	        if("-" in addressString):
	            splitted = addressString.split("-")
	            return splitted[0].strip(),splitted[1].strip()
	        return "",addressString.strip()

	@staticmethod
	def getSize(tag):
	    if tag == None:
	        return None
	    else:
	        return re.sub("m²", "", tag.text)

	@staticmethod
	def getAds(soup):
		#r  = requests.get(url)
		#data = r.text
		#soup = BeautifulSoup(data, "html.parser")

		#pickle.dump( soup, open( "save.p", "wb" ) )

		soup = pickle.load( open( "BlocketRequest.p", "rb" ) )
		items = []

		for html_item in soup.select("#item_list > div"):
		    item = {}
		    item['title'] = BlocketParser.getFirstOrDefault(html_item.select('.item_link.xiti_ad_heading')).text.strip()
		    item['link'] = BlocketParser.getFirstOrDefault(html_item.select('.item_link.xiti_ad_heading'))['href']
		    imageLink = BlocketParser.getFirstOrDefault(html_item.select('.sprite_list_placeholder > a'))
		    item['image'] = BlocketParser.getImage(imageLink)
		    item['price'] = BlocketParser.getPrice(BlocketParser.getFirstOrDefault(html_item.select('.li_detail_params.monthly_rent')))
		    item['rooms'] = BlocketParser.getRoomCount(BlocketParser.getFirstOrDefault(html_item.select('.li_detail_params.first.rooms')))
		    item['kommune'],item['address'] = BlocketParser.getAddress(BlocketParser.getFirstOrDefault(html_item.select('.address')))
		    item['size'] = BlocketParser.getSize(BlocketParser.getFirstOrDefault(html_item.select('.li_detail_params.size')))
		    items.append(item)
		return items
