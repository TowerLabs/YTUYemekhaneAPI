# -*- coding: utf-8 -*-
from __future__ import print_function
from pyquery import PyQuery as pq 
import datetime, cgi, json, os

class YemekhaneAPI:	

	def __init__(self):
		now 	= datetime.datetime.now()
		month 	= now.strftime("%m") 
		year 	= now.strftime("%Y") 
		month 	= "%01d" % (int(month),)		
		self.url	= "http://www.sks.yildiz.edu.tr/yemekmenu/" + str(month) + "/" + year
		self.foods 	= []

	def parse(self):
		parser  = pq(url=self.url)
		parser('div#menu_background').each(lambda i, n: self.data_append(n))

	def data_append(self,obj):
		parser_obj 	= pq(obj)
		date 		= parser_obj('div#menu_header div:first').html()
		root_lunch  = parser_obj('div#menu_container div#menu_slider div.one_menu')
		main_lunch 	= root_lunch('div.one_lunchMainMenu').html()
		alt_lunch 	= root_lunch('div.one_lunchAltMenu').html()
		main_dinner = root_lunch('div.one_dinnerMainMenu').html()
		alt_dinner  = root_lunch('div.one_dinnerAltMenu').html()
		one_day		= {"main_lunch":self.replace_tags(main_lunch),"alt_lunch":self.replace_tags(alt_lunch),"main_dinner":self.replace_tags(main_dinner),"alt_dinner":self.replace_tags(alt_dinner)}
		self.foods.append({date:one_day})

	def replace_tags(self,str):
		try:
			return str.replace("<br/>",",").replace("<br/ >",",").replace("<br />",",").rstrip(',')
		except:
			return ""

	def return_json(self):
		return json.dumps(self.foods)
	
	def write_json(self):
		if os.path.isfile("example.json"):
			os.remove("example.json")
		file = open("example.json",'w+')
		file.write(json.dumps(self.foods))
		file.close()

if __name__ == "__main__":
	API = YemekhaneAPI()
	API.parse()
	#print(API.return_json())
	API.write_json()