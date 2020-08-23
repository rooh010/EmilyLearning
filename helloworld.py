# simple print statement
print("hello world")



# function
def printme (str): 
    "this prints a string you pass to it"
    print(str)


# function
def printme2 (sometext): 
    print(sometext)


# call function
printme("test")

printme2("test2")


# class
class GradeBook:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def gradefunction(self):
        print("my name is " + self.name + " and my grade is " + str(self.grade))

    def namelength(self):
        a = len(self.name)
        print("Length of name is " + str(a))

grade1 = GradeBook("Emily", "A+")

grade1.name = "Emily F"

grade1.gradefunction()


#new line
print("\n")

grade1.namelength()

print("\n")

# return statement    
def add(a, b): 
    return a + b 
  
def is_true(a): 
    return bool(a) 
  
# calling function 
res = add(2, 3) 
print("Result of add function is {}".format(res)) 
  
res = is_true(2<5) 
print("\nResult of is_true function is " + str(res)) 


