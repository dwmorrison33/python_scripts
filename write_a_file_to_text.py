from sys import argv

script, filename = argv

target = open(filename, 'w')

print "I'm going to ask you 3 questions."

x = raw_input("What's your first name: ")
y = raw_input("What's your last name: ")
z = raw_input("What's your age: ")

target.write(x)
target.write(y)
target.write(z)

target.close()
