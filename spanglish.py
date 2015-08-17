el = "El "
spang = "o"

print "You can translate any word into spanglish"
orig = raw_input("Enter a word: ")
new_word = el + orig + spang

if len(orig) > 0 and orig.isalpha():
    print new_word
else:
    print "nice try, actually enter a word next time!!!!"
