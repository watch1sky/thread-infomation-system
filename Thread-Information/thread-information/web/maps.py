# -*- coding:utf-8 -*-
import json
import pygal.maps.world
from pygal.style import RotateStyle

filename = 'country.json'
with open(filename, 'r') as file:
    ip_data = json.load(file)
ip_info = {}
for ip in ip_data:
    country_id = str(ip)
    ip_info[country_id] = ip_data[ip]

sty=RotateStyle('#336699')
worldmap_chart = pygal.maps.world.World(style = sty)
worldmap_chart.title = 'ips in maps'
worldmap_chart.add('ips', ip_info)
worldmap_chart.render_to_file('/static/images/ips_map.svg')