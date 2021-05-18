print "You enter a room with two doors. Do you choose door 1 or 2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating cheesecake. What do you do?"
    print "1. Take the cake."
    print "2. Shake the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        
elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina. You think of..."
    print "1. The buddhist palm."
    print "2. The axe gang."
    print "3. Pig sty alley."
    
    enlightenment = raw_input("> ")
    
    if enlightenment == "1" or enlightenment == "2":
        print "You strive for power of body, not mind."
    else:
        print "You too can maybe one day become a kung fu master."
        
else:
    print "You stumble around and fall on a knife and die. Good job!"