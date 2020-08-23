# simple print statement
print("hello world")



# function
def printme (str): 
    "this prints a string you pass to it"
    print(str)
    return

# function
def printme2 (str): 
    print(str)
    return

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

grade1 = GradeBook("Emily", "A+")
grade1.gradefunction()


