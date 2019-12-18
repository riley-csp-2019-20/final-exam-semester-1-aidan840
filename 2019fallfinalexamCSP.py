#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Aidan Mckinney
#Date
# 12/18/2019


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl 

#create turtle
sk = trtl.Turtle()
sk.shape("turtle")
sk.turtlesize(1)

#movement functions
def sk_up():        #This makes the turtle move up when you press the up arrow
    sk.setheading(90)
    sk.forward(10)

def sk_down():      #This makes the turtle move down when you press the down arrow
    sk.setheading(270)
    sk.forward(10)

def sk_right():     #This makes the turtle move right when you press the right arrow
    sk.setheading(0)
    sk.forward(10)

def sk_left():      #This makes the turtle move left when you press the left arrow
    sk.setheading(180)
    sk.forward(10)


def sk_space():    #when youb press space the sceen clears
    sk.clear()

def sk_u():         #when youb press u the pen goes up
    sk.penup()
   
def sk_d():         #when you press d the pen goes down
    sk.pendown()


def sk_o():        #when youb press o the pensize increases
    sk.pensize(+7)

def sk_p():       #when youb press p the pensize decreases 
    sk.pensize(1)







#color/drawing functions



#create screen
wn = trtl.Screen()
wn.bgcolor("light blue")
wn.onkeypress(sk_up,"Up")
wn.onkeypress(sk_down,"Down")
wn.onkeypress(sk_left,"Left")
wn.onkeypress(sk_right,"Right")
wn.onkeypress(sk_space,"space")
wn.onkeypress(sk_u,"u")
wn.onkeypress(sk_p,"p")
wn.onkeypress(sk_o,"o")
wn.onkeypress(sk_d,"d")





#bind to keypresses


#listen
wn.listen()

#mainloop

wn.mainloop()
wn.bgcolor("light blue")