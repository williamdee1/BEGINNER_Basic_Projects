name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#inches in centimeters
cm_conversion = float(2.54)
height_in_centimeters = float(height * cm_conversion)

#lbs to kgs
kg_conversion = float(1/2.205)
weight_in_kgs = weight * kg_conversion

print "Let's talk about %s." %name
print "He's %d inches tall." %height
print "He's %d centimeters tall." %height_in_centimeters
print "He's %d pounds heavy." %weight
print "He's %d kilograms heavy." %weight_in_kgs
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee" %teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(age, height,weight, age + height + weight)
print "Kg conversion is %r." %round(kg_conversion,[2])
print "Cm conversion is %f." %round(cm_conversion)