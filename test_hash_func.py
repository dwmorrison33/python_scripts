import urllib2

def get_page(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html

def hash_string(keyword, buckets):
    h = 0
    for char in keyword:
        h = h + ord(char)
    return h % buckets

def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv] += 1
            keys_used.append(w)
    return results

words = get_page("https://en.wikipedia.org/wiki/Jesus").split()
count = test_hash_function(hash_string, words, 100)
print count
