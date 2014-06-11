"""
Copyright (C) 2014 TowerLabs

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the
Free Software Foundation, Inc., 51 Franklin Street,
Fifth Floor, Boston, MA  02110-1301, USA.
"""
#  -*- coding: utf-8 -*-
from __future__ import print_function
from pyquery import PyQuery as pq
import datetime
import time
import cgi
import json
import os


class YemekhaneAPI:

    def __init__(self):
        now = datetime.datetime.now()
        month = now.strftime("%m")
        year = now.strftime("%Y")
        month = "%01d" % (int(month),)
        self.url = "http://www.sks.yildiz.edu.tr/yemekmenu/"
        self.url += str(month) + "/" + year
        self.foods = []

    def parse(self):
        parser = pq(url=self.url)
        parser('div#menu_background').each(lambda i, n: self.data_append(n))

    def data_append(self, obj):
        parser_obj = pq(obj)
        date = parser_obj('div#menu_header div:first').html()
        root_lunch = parser_obj('div#menu_container div#menu_slider')
        root_lunch = parser_obj('div.one_menu')
        main_lunch = root_lunch('div.one_lunchMainMenu').html()
        alt_lunch = root_lunch('div.one_lunchAltMenu').html()
        main_dinner = root_lunch('div.one_dinnerMainMenu').html()
        alt_dinner = root_lunch('div.one_dinnerAltMenu').html()
        one_day = {
            "main_lunch": self.replace_tags(main_lunch),
            "alt_lunch": self.replace_tags(alt_lunch),
            "main_dinner": self.replace_tags(main_dinner),
            "alt_dinner": self.replace_tags(alt_dinner)
        }
        self.foods.append({date: one_day})

    def replace_tags(self, str):
        try:
            str = str.replace("<br/>", ",")
            str = str.replace("<br/ >", ",")
            str = str.replace("<br />", ",")
            str = str.rstrip(',')
            return str
        except:
            return ""

    def return_json(self):
        return json.dumps(self.foods)

    def write_json(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        file = open(dir+'/'+str(int(time.time()))+'.flist', 'w+')
        file.write(json.dumps(self.foods))
        file.close()


if __name__ == "__main__":
    API = YemekhaneAPI()
    API.parse()
    #print(API.return_json())
    API.write_json()
