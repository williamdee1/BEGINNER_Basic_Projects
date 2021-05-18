people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."   
elif cars < people:
    print "We should ride horseback instead."
else:
    print "We can't decide, we could stay here."

if buses > cars:
    print "The buses are taking over."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."
    
if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

## The elif statement allows you to check multiple expressions 
## for TRUE and execute a block of code as soon as one of the 
## conditions evaluates to TRUE. 