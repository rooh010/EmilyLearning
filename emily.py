# print("hello")

# name2 = "Emily"

# print(name2 + " this is my name " + name2 + " " + str(15435345345))

# print("string")



def quizquestions():
    name = input ("Enter your name: ")
    print()
    age = input ("Enter you age: ")
    print()
    print ("Hello", name," you are", str(age), " years old " "have fun while doing the quiz")

# quizquestions() 

def printme(sometext):
    print("here is sometext: " + sometext)

def age(youragehere):
    olderage = youragehere + 10
    print("in 10 years you will be " + str(olderage) + " years old")

# create blank list

emilyslist = []
dadlist = ["pug","husky","jack russell","yorkie"]

# add item to list

def addtomylist(someitem):
    emilyslist.append(someitem)

# print list

def printmylist():
    print(emilyslist)

addtomylist("d")
addtomylist("dog")
addtomylist("j")
addtomylist("mim")
addtomylist("dada")

# print(str(len(emilyslist)))


def printlist(somelist):
    listlength = len(somelist)
    i = 0
    while i < listlength:
        print(somelist[i] + " somewords")
        i += 1

printlist(emilyslist)













