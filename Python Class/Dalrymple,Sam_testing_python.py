# BASIC
for i in range (1, 151):
    print (i)
    

# This is here to creat a space between the outputs and will be used throughout
print ("                            ")

# Multiples of five
for i in range (1, 1001):
    if (i % 5 == 0):
        print (i)
        
# space
print ("                            ")

# Counting the dojo way
for i in range (1, 101):
    if (i % 10 == 0):
        print ("Coding Dojo")
    elif (i % 5 == 0):
        print ("Coding")
    elif (i % 5 != 0 or i % 10 != 0):
        print (i)
        
# space
print ("                            ")

# Whoa that suckers huge
sum = 0

for i in range (1, 500001, 2):
    sum = sum + i
print (sum)

# space
print ("                            ")

# countdown by fours
for i in reversed(range(1, 2018)):
    if (i % 4 == 0):
        print (i)

# space
print ("                            ")

# flexible counters
lowNum = 1
highNum = 100
mult = 3

for i in range (lowNum, highNum):
    if (i % mult == 0):
        print (i)