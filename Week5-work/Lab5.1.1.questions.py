numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "Joe"
ages = []
months = ('January', 'February', 'March')
book = {}
stuff = [12, 'Fred', False, {}]
someone = dict(firstname = "Joe")
me = {
    "firstName": "Michael",
    "learning" : [{

        "CourseName" : "pands",
        "Semester": 1
    },{
        "CourseName" : "data",
        "Semester": 2
    }
    ]
}

print(type(numberOfQuestions))
print(type(averageAge))
print(type(debugMode))
print(type(name))
print(type(ages))
print(type(months))
print(type(months[1]))
print(type(book))
print(type(stuff))
print(type(stuff[2]))
print(type(someone))
print(type(someone["firstname"]))
print(type(me))
print(type(me["learning"]))
print(type(me["learning"][0]["Semester"]))