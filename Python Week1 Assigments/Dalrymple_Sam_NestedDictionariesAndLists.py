# 1 - this was very straight forward
x = [ [5,2,3], [15,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Bryant'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]


# 2 - little moree difficult had to ask for a bit of help but it was mainly because I was just looking at it the wrong way (sorta)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary1(dictList):
    for i in dictList:
        itemLine = ""
        for val1, val2 in i.items():
            itemLine += f"{val1} - {val2}, "
        print(itemLine[:-2])

iterateDictionary1(students)

# 3 - idk why this one was easier for me than the last one but it was. included both first_name and last_name as outputs to show both work
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iteranteDictionary2(keyName, dictList2):
    for i in dictList2:
        if keyName in i:
            print (i[keyName])

iteranteDictionary2('first_name', students)
iteranteDictionary2('last_name', students)

# 4 - this one tripped me up because I wasn't using .items at first and after some w3schools reading I found what I needed to fix it
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dictlist3):
    for val1, val2 in dictlist3.items():
        print (f"{len(val2)}, {val1}")
        for i in val2:
            print(i)
        print()

printInfo(dojo)