#!/usr/local/bin/python3

import json

data_file="bar.json"

with open(data_file) as data_file:
	data = json.load(data_file)

# result in an array of records
items=data["items"]
#print(items)

for i in items:
	tags=i["tags"]
	if ("70s" in tags):
		print(i)

