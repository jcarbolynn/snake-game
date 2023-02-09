from turtle import Turtle
import random

class Food(Turtle):

  # inheritance: snake is a turtle, food is a food which inherits from turtle
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.color("green")
    self.speed(0)
    self.refresh()

  def refresh(self):
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    self.goto(random_x, random_y)
    
