from random import randint


def start():
    print "Welcome to the Price is Right"

    seat_numbers = range(1, 500)
    contestants = [seat_numbers.pop(randint(0,len(seat_numbers)-1)) for i in range(4)]

    print "Lets Welcome the contestants!"
    for i, num in enumerate(contestants):
        print "Come on down Contestant %s in seat %s, you're the next contestant on the price is right" % (i+1, num)

def cont_bids():

    cont_bids= []
    for i in range(4):
        cont_guess = int(raw_input("Contestant %s, What do you bid? " % (i + 1)))
        cont_bids.append(cont_guess)

    return cont_bids

def create_prize():

    return randint(500, 2500)


def winning_bidder():

    bids = cont_bids()
    price = create_prize()
    print price
    valid_bids = []
    for bid in bids:
        if bid == price:
            print "You guessed the price exactly, you win an extra $500, now come on up!"
            return
        elif bid > price:
            pass
        else:
            valid_bids.append(bid)

    if len(valid_bids) == 0:
        print "You all overbid"
    else:
        winner = max(valid_bids)
        print "%s is the winner!" % winner

def spin_value():

    div_by_5 = []
    for i in range(1,100):
        if i % 5 == 0:
            div_by_5.append(i)
    return div_by_5[randint(0, len(div_by_5)-1)]

def spin_the_wheel():
    spin = spin_value()
    print "Your first spin: %s" % spin
    if spin < 100:
        print "spin again?"
        if raw_input() == "yes":
            spin += spin_value()
            print "You new total: %s" % spin
    if spin > 100:
        print "Oh too bad."
    if spin == 100:
        print "You win $1000"


print spin_the_wheel()



#start()
#print "*" * 50

#for round in range(1, 6):
#    print "round", round
#    winning_bidder()
