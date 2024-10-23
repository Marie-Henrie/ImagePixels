import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Simple Cat Drawing")
screen.bgcolor("white")

# Setup turtle
t = turtle.Turtle()
t.speed(3)  # Adjust the speed of the drawing

# Function to draw a circle (useful for the head and eyes)
def draw_circle(radius, color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw the cat's head
draw_circle(100, "gray", 0, -100)

# Draw the cat's left ear
t.penup()
t.goto(-70, 50)
t.setheading(60)
t.pendown()
t.begin_fill()
t.goto(-120, 100)
t.goto(-50, 120)
t.goto(-70, 50)
t.end_fill()

# Draw the cat's right ear
t.penup()
t.goto(70, 50)
t.setheading(120)
t.pendown()
t.begin_fill()
t.goto(120, 100)
t.goto(50, 120)
t.goto(70, 50)
t.end_fill()

# Draw the left eye
draw_circle(15, "white", -50, -30)

# Draw the right eye
draw_circle(15, "white", 50, -30)

# Draw the pupils
draw_circle(7, "black", -50, -25)
draw_circle(7, "black", 50, -25)

# Draw the nose
t.penup()
t.goto(0, -50)
t.pendown()
t.color("pink")
t.begin_fill()
t.circle(10)
t.end_fill()

# Draw the whiskers
t.penup()
t.goto(-50, -60)
t.setheading(0)
t.pendown()
t.forward(70)

t.penup()
t.goto(-70, -70)
t.setheading(20)
t.pendown()
t.forward(100)

t.penup()
t.goto(-70, -50)
t.setheading(-20)
t.pendown()
t.forward(100)

# Hide the turtle cursor
t.hideturtle()

# Keep the window open
screen.mainloop()
