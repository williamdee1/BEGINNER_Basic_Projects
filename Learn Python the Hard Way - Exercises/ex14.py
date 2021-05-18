from sys import argv

script, user_name, favourite_colour = argv
prompt = 'Type here dumbass '

print "Hi %s, I'm the %s script, I like %s." % (user_name, script, favourite_colour)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % (user_name)
likes = raw_input(prompt)

print "Where do you live %s and do you like %s?" % (user_name, favourite_colour)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice. 
""" % (likes, lives, computer)

