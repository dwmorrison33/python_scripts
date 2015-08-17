from random import randint

lottery = []
megaball = [randint(1,15)]
for i in range(5):
    lottery.append(randint(1,75))
    lottery.sort()

print lottery, megaball
