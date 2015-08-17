import urllib2

def get_page(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html

print get_page('http://www.codewithchrist.com/')
