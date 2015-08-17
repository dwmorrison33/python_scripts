import urllib2

def get_page(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html


def get_next_target(page):

    start_link = page.find("<a href=")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

url, endpos = get_next_target(get_page('http://www.codewithchrist.com/'))

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break

print_all_links(get_page('http://www.codewithchrist.com/'))
# if I change the call of print_all_links to a pages source and get_next_target to the pages source, it will return all the links on that page
# I still need to figure out how to input the url link in there to save space
# this <a href="test1">link 1 </a> is <a href="test2">link 2 </a> is <a href="test3">link 3 </a>
