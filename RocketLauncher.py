import turtle as t
# Making a game board
t.showturtle()
t.speed(0)
t.penup()

# Circle1
t.goto(200,0)
t.dot(50)
# Circle2
t.goto(300,200)
t.dot(50)
# Circle3
t.goto(300,-200)
t.dot(50)

t.goto(-200,0)
t.pendown()
t.pencolor("red")
# Getting input data from the user
rotation = int(input("Enter the degree of rotation..."))
distance = int(input("Enter the distance...")) 
t.left(rotation)
t.forward(distance)

t.done()