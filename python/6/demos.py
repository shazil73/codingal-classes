import turtle

turtle.Screen().bgcolor("lightblue")

gg = turtle.Screen()

gg.setup(width=800, height=600)

gg.title("Turtle Graphics making a star")

board = turtle.Turtle()


board.forward(200)
board.left(120)

board.forward(200)
board.left(120)

board.forward(200)
board.right(150)

board.penup()
board.forward(100)

board.pendown()
board.right(90)

board.forward(200)
board.right(120)

board.forward(200)
board.right(120)

board.forward(200)
board.right(120)
