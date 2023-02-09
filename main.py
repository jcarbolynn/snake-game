from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# when tracer is off (0) nothing prints, screen wont refresh until you call update
screen.tracer(0)

# oop so if anything goes wrong you know where the problem is
snake = Snake()
food = Food()
scoreboard = Score()

# listen to accept user feedback
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
  screen.update()
  time.sleep(.1)

  snake.move()

  # detect collision with food
  # distance from first turtle segment in snake to food item (which inherits from turtle)
  if snake.head.distance(food) < 15:
    scoreboard.keep_score()
    food.refresh()
    snake.grow()

  # detect collision with wall
  if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
    game_on = False
    scoreboard.game_over()

  # detect collision with tail
  # slice instead of using if statement to avoid checking against first segment
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      game_on = False
      scoreboard.game_over()
      
  # for segment in snake.segments:
  #   if segment == snake.head():
  #     pass
  #     # otherwise head is always within 10  pixels of snake segment
  #   elif snake.head.distance(segment) < 10:
  #     game_on = False
  #     scoreboard.game_over()



screen.exitonclick()
