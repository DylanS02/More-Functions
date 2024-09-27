from turtle import *

# Square

def square(size, sq_color):
    # Copy-and-paste your square function here
    pass
    color(sq_color)
    begin_fill()
    forward(size)
    right(90) 
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    end_fill()

def row(number, sq_size, sq_color):
    # For Exercise 3, new code goes inside this function
	pass
	for i in range(4):
		square(sq_size, "red")
		penup()
		forward(sq_size)
	

### Do not modify anything below this line
# Draw board

penup()
goto(-200, 200)
pendown()
square(400, "black")
row(4, 400/4, "red")

done()
