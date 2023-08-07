from turtle import Turtle, Screen
# from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# when tracer is off (0) nothing prints, screen wont refresh until you call update
screen.tracer(0)

segments = []
for _ in range(3):
  snake_seg = Turtle()
  snake_seg.shape("square")
  snake_seg.color("white")
  # snake_seg.setx(10-(_*20))
  snake_seg.penup()
  snake_seg.setx(-(_*20))
  segments.append(snake_seg)
# update after snake printed so it will not show up piece by piece, all displayed at once


game_on = True
while game_on:
  #move each segment, loop through each segment and move it forward by an ammount
  screen.update() # snake moves as one piece, all 3 segments forward before update triggered
  # move delay up here so only delays after all 3 pieces moved forward
  time.sleep(.1)
  # for seg in segments:
  #   seg.forward(10)
  #   # # adds 1s delay after each piece moves
  #   # time.sleep(1)
  # replace above for loop with below because above only lets snake move forward, instead have each segment move to where segment before was
  # for seg_num in range(start=len(segments) -1, stop=0, step= -1):
  for seg_num in range(len(segments) -1, 0, -1):
    new_x = segments[seg_num -1].xcor()
    new_y = segments[seg_num -1].ycor()
    segments[seg_num].goto(new_x, new_y)

  segments[0].forward(20)
  

screen.exitonclick()
