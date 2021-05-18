i = 0
numbers = []
variable = 6
increment = 2


while i < variable:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = i + increment
    print "Numbers now: ", numbers
    print "At the bottom i is %d." % i

print "The numbers: "

for num in numbers:
    print num
    
    
