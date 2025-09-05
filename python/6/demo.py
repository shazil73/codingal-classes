import turtle

turtle.Screen().bgcolor("lightblue")

gg = turtle.Screen()

gg.setup(width=800, height=600)

gg.title("Turtle Graphics Demo")

board = turtle.Turtle()

for i in range(0, 4):
    board.forward(200)
    board.right(90)