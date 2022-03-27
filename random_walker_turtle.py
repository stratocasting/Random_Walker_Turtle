import turtle as t
import random
game_over = False
tim = t.Turtle()
tim.shape("circle")
directions = [0, 90, 180, 270,]
tim.speed(2000)
tim.pensize(14)
########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
while not game_over:
    tim.color(random.choice(colours))
    tim.forward(50)
    tim.left(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
game_over = True
