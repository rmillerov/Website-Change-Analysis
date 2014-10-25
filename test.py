import urllib2, json

test_url = 'openviewpartners.com'

response = urllib2.urlopen('http://web.archive.org/cdx/search/cdx?url=' + test_url + '&output=json&limit=3')
#print response.read()
works = json.load(response)[1][1]
print works