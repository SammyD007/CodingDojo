# 1 - pretty easy one, to be expected from being the first part
def countdown(num):
    cdList = []
    for i in range(num, -1, -1):
        cdList.append(i)
    print (cdList)

countdown(5)

# 2 - I had some trouble with this one and I actually don't know if it works the way intedned so if not I may need a little talk through what was expected
def printAndReturn(liOne, liTwo):
    prntandretList = []
    prntandretList.extend([liOne, liTwo])
    print (prntandretList[0])
    return prntandretList[1]

printAndReturn(4,6)

# 3 - expected this to be harder when reading it but it basically worked as soon as I typed what I talked through it
def firstPlusLength(list):
    value = list[0] + len(list)
    print (value)

firstPlusLength([1,2,3,4,5,6,7,8,9])

# 4 - I feel like there is a much cleaner or better way to do this but I got it to work and ran a few lists through it and it seems to work right so I will take it lol
def valuesGreaterThanSecond(list2):
    if len(list2) < 2:
        return False
    
    valueTwo = list2[1]
    newList = []
    for i in list2:
        if i > valueTwo:
            newList.append(i)
    print (newList)
    print (len(newList))

valuesGreaterThanSecond([5,4,4,5,6,23,5,4])