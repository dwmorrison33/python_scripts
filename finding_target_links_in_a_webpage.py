page = '''<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Udacity</title>
</head>
<body>
<h1>Udacity</h1>
<p><b>Udacity</b> is a private institution of
<a href="http://www.wikipedia.org/wiki/Higher_education">higher education founded by</a> <a href="http://www.wikipedia.org/wiki/Sebastian_Thrun">Sebastian Thrun</a>, David Stavens, and Mike Sokolsky with the goal to provide university-level education that is "both high quality and low cost".</p>
<p> It is the outgrowth of a free computer science class offered in 2011 through Stanford University. Currently, Udacity is working on its second course on building a search engine. Udacity was announced at the 2012 <a href="http://www.wikipedia.org/wiki/Digital_Life_Design">Digital Life Design</a> conference.</p>
</body>
</html>'''

# I am looking if to see if these links appear in this html code
# If -1 appears is printed in my terminal, the page does not exist
# Otherwise it will print the index of where that page begins

print page.find("http://www.w3.org/1999/xhtml")
print page.find("http://www.wikipedia.org/wiki/Higher_education")
print page.find("www.wikipedia.org/wiki/Sebastian_Thrun")
print page.find("both high quality and low cost")
print page.find("http://www.wikipedia.org/wiki/Digital_Life_Design")
