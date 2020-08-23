import turtle
t=turtle.Pen()
t.fillcolor('Purple')
t.begin_fill()
t.pencolor("Pink")
t.speed(5)
for i in range (4):
    t.forward(100)
    t.left(90)
t.end_fill()
t.pencolor("White")
t.left(180)
t.forward(75)
t.speed(10)
for i in range (50):
    t.pencolor("Green")
    t.forward(100)
    t.left(190)
    t.pencolor("Blue")
    t.forward(100)
    t.left(190)
    t.pencolor("Pink")
    t.forward(100)
    t.left(190)
    
    
