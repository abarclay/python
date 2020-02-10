#!/usr/local/bin/python3

# You are developing a web-service that will query a remote repository
# (imdb, etc. etc) which will return a large quantity of results
# We want to search the results by tag and return the results
#
# Because there is a very large quantity of results, the search method
# must be a generator in order to make efficient use of memory
#
# the second method, "first" will return just the first result that matches
# the tag and that is all
# 
# for the purposes of this question, you can assume that the results
# are available in a file called results.json

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
