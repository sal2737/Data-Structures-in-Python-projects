#  File: USFlag.py
#  Description: Draws the American flag at a size specified by the usual
#  Student's Name: Sam Limerick
#  Student's UT EID: sal2737
#  Course Name: CS 313E 
#  Unique Number: 50595
#
#  Date Created: 2/11/16
#  Date Last Modified: 2/13/16
     
import math
import turtle

def main():

	#Prompt user to enter hoist of flag in pixels
	hoist = int(input("Enter your desired vertical height of the flag in pixels: "))
	
	#diameter of star =
	#assign dimensions of the flag based on user input to variables for storage
	flyFlag = 1.9 * hoist
	flyCanton = .76 * hoist	
	topBarFly = flyFlag - flyCanton
	heightCanton = .5385 * hoist
	spacingOfStars = .1 * heightCanton
	colorBarHeight = .0769 * hoist
	diameterOfStar = .8 * colorBarHeight
	
	#Initialize screen and setup
	ttl = turtle.Turtle()
	screen = turtle.Screen()
	screen.title("CS 313E Assignment 2")
	turtle.setup(flyFlag + 200, hoist + 200)
	
	#draw outline of flag
	ttl.penup()
	ttl.goto((-.5 * flyFlag), (.5 * hoist))
	ttl.pendown()
	ttl.forward(flyFlag)
	ttl.right(90)
	ttl.forward(hoist)
	ttl.right(90)
	ttl.forward(flyFlag)
	ttl.right(90)
	ttl.forward(hoist)
	ttl.penup()

	#draw canton
	ttl.right(90)
	ttl.begin_fill()
	ttl.color('blue')
	ttl.forward(flyCanton)
	ttl.right(90)
	ttl.forward(heightCanton)
	ttl.right(90)
	ttl.forward(flyCanton)
	ttl.right(90)
	ttl.forward(heightCanton)
	ttl.right(90)
	ttl.end_fill()

	#initialize bar drawing
	ttl.forward(flyCanton)
	ttl.color('red')
	
	#draw top bars
	for i in range(4):
		ttl.begin_fill()
		ttl.forward(topBarFly)
		ttl.right(90)
		ttl.forward(colorBarHeight)
		ttl.right(90)
		ttl.forward(topBarFly)
		ttl.right(90)
		ttl.forward(colorBarHeight)
		ttl.end_fill()
		ttl.right(180)
		ttl.forward(2 * colorBarHeight)
		ttl.left(90)
		
	#prepare to draw bottom bars
	ttl.right(180)
	ttl.forward(flyCanton)
	ttl.left(90)
	#draw bottom bars
	
	for i in range(3):
		ttl.begin_fill()
		ttl.forward(colorBarHeight)
		ttl.left(90)
		ttl.forward(flyFlag)
		ttl.left(90)
		ttl.forward(colorBarHeight)
		ttl.left(90)
		ttl.forward(flyFlag)
		ttl.end_fill()
		ttl.left(90)
		ttl.forward(2 * colorBarHeight)
		
	#keeps window from closing once program terminates
	turtle.done()
main()