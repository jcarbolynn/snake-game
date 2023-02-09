from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')

class Score(Turtle):

  # inheritance: snake is a turtle, food is a food which inherits from turtle
  def __init__(self):
    super().__init__()
    self.score = 0
    self.hideturtle()
    self.penup()
    self.pencolor("white")
    self.setposition(-270, 270)
    self.display()

  def display(self):
    self.clear()
    self.write(f"Score: {self.score}", False, align = ALIGNMENT, font = FONT)

  def keep_score(self):
    self.score += 1
    self.display()
    # print(self.score)

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER", align = ALIGNMENT, font = FONT)
  # def refresh(self):
  #   self.setposition(-0, 270)
  #   # self.display()
    
