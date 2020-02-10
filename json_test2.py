#!/usr/local/bin/python3

import json

class SearchByTag:

	def __init__(self, data_file, query_tag):
		with open(data_file) as data_file:
			self._data = json.load(data_file)
		self.query = query_tag

	def search(self):
		# results in an array of records
		try:
			items=self._data["items"]
		except:
			return
		#print(items)
		for item in items:
			#print(item)
			try:
				tags=item["tags"]
			except:
				return
			if (self.query in tags):
				#print("found")
				yield item
		return

	def first(self):
		for x in self.search():
			return(x)

search = SearchByTag("results.json","70s")
first = search.first()
print(first)
#quit()

print("---------------")
data=search.search()
for i in data:
	print(i)
