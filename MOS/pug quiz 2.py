score = 0

print ("WELCOME TO MY QUIZ!")
print()
      
print ("The topic is pugs")
print()

name = input ("Enter your name: ")
print()
age = input ("Enter you age: ")
print()
print ("Hello", name, "have fun while doing the quiz")

print()
score = int(0)

print (" 1. What is a group of pugs called?")
answer1 = input ("Make your choice: ")

print (answer1.lower())
# answer printed with lower

if answer1 == "Grumble" :
    print()
    print ("Well done, you got it right!")
    score = score + 1
    print ("Total Score = ", score)
# elif statement
elif answer1 == "grumble" :
    print()
    print ("Well done, you got it right!")
    score = score + 1
    print ("Total Score = ", score)
else:
    print()
    print ("Sorry, you got it wrong")
    print ("Total Score = ", score)

print()
print (" 2. What are  pugs known for? ")
answer2 = input ("Make your choice: ")
print (answer2)

if answer2 == "Curly tails" or answer2 == "curly tails" :
    print()
    print ("Well done, you got it right!")
    score = score + 1
    print ("Total Score = ", score)
else:
    print()
    print ("Sorry, you got it wrong")
    print ("Total Score = ", score)
    
print()
print (" 3. What is the German word for pugs?")
answer3 = input ("Make your choice: ")
print (answer3)

if answer3 == "Mops" or answer3 == "mops" :
    print() 
    print ("Well done, you got it right!")
    score = score + 1
    print ("Total Score = ", score)
else:
    print()
    print ("Sorry, you got it wrong")
    print ("Total Score = ", score)
    
print()
print (" 4. In which century were pugs brought from China to Europe?")
answer4 = input ("Make your choice: ")
print (answer4)

if answer4 == "16th" or answer4 == "Sixteenth" :
    print()
    print ("Well done, you got it right!")
    score = score + 1
    print ("Total Score = ", score)
else:
    print()
    print ("Sorry, you got it wrong")
    print ("Total Score = ", score)
    
print()
print (" 5. Where did pugs originate from ?")
answer5 = input ("Make your choice: ")
print (answer5)

if answer5 == "China" or answer5 == "china" :
    print()
    print ("Well done, you got it right!")
    score = score + 1
    print ("Total Score = ", score)
else:
    print()
    print ("Sorry, you got it wrong.  Thanks for taking the quiz!")
    print ("Total Score = ", score)

    
