from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.001

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= 0.8

    def bounce_x(self):
        self.x_move *= -0.8
        self.move_speed = 0.08

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.08
        self.bounce_x()
