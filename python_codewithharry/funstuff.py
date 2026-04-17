# import turtle
# colors = ['pink', 'purple', 'lightblue', 'turquoise', 'grey', 'yellow', "beige"]
# t = turtle.Pen()
# turtle.bgcolor('black')
# t.speed(0.5) # Fastest speed

# for x in range(200):
#     t.pencolor(colors[x % 7]) # Cycles through your list of 6 colors
#     t.width(x/100 + 1)         # Lines get thicker as it grows
#     t.forward(x)               # Moves forward by x (0, 1, 2...)
#     t.left(59)                 # Turns 59 degrees to create the spiral


# import turtle

# t = turtle.Turtle()
# t.speed(0)
# t.width(3)

# def draw(x, y):
#     t.goto(x, y)

# def change_red(): t.color("red")
# def change_blue(): t.color("blue")
# def clear_screen(): t.clear()

# turtle.listen()
# t.ondrag(draw) # Drawing while dragging
# turtle.onkey(change_red, "r")
# turtle.onkey(change_blue, "b")
# turtle.onkey(clear_screen, "c")

# turtle.done()

