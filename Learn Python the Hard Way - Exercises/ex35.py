from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn how to type a number...")
    
    if how_much < 50:
        print "Good, you're not greedy, you win"
        exit(0)
    
    else:
        dead ("Too much, deadsies!!")

def bear_room():
    print "There's a bear here..."
    print "The bear has a bunch of honey..."
    print "He's sitting in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    while True:
        next = raw_input("what do you want to do now > ")
        
        if next == "take honey":
            dead("The bear looks at you and then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved away from the door. You can proceed."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear charges, angry at your taunts, ripping your legs off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means...try again (sigh)"
        
def ctulu_room():
        print "Here you see the great evil eye of Ctulu."
        print "It stares deep into your soul."
        print "Do you run or eat your own head?"
        
        next = raw_input("> ")
        
        if "run" in next:
            start()
        elif "head" in next:
            dead("Why would you do that... You're dead now, obvs...")
        else:
            ctulu_room()
            
def dead(why):
        print why, "Nice work!"
        exit(0)
            
def start():
        print "You are in a dark room."
        print "There is a door to your right and left."
        print "Which door do you take?"
        
        next = raw_input("> ")
        
        if next == "left":
            bear_room()
        
        if next == "right":
            ctulu_room()
        
        else:
            dead("You stumble into a corner of magnets, dragging your metal body inexoribly onto large spikes that slowly impale you.")
     
start()
