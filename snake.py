from turtle import Turtle
START_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  # create_snake, add_segment, grow interesting
  def create_snake(self):
    for position in START_POS:
      self.add_segment(position)

  # add new segment to snake
  def add_segment(self, position):
    snake_seg = Turtle()
    snake_seg.shape("square")
    snake_seg.color("white")
    snake_seg.penup()
    snake_seg.goto(position)
    self.segments.append(snake_seg)

  def grow(self):
    # in python use negative number to start from end of list
    # position is method in turtle class
    self.add_segment(self.segments[-1].position())
  
  def move(self):
    for seg_num in range(len(self.segments) -1, 0, -1):
      new_x = self.segments[seg_num -1].xcor()
      new_y = self.segments[seg_num -1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.segments[0].forward(MOVE_DISTANCE)
  
  def up(self):
    #snake not allowed to go back on itself
    # why does self.head.heading() work
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
      self.move()
    
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
      self.move()
  
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
      self.move()
  
  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
      self.move()
