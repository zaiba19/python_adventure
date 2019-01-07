#This program makes a colorful hexagon
import turtle
wn =turtle.Screen()

tod =turtle.Turtle()

for color in ['red','orange','yellow','green','blue','purple']:
	tod.color(color)
	tod.forward(100)
	tod.left(60)
