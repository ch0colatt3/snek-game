import turtle

import time
import random

delay = 0.1
#Score
score = 0
high_score=0

#screen
wn = turtle.Screen()
wn.title("a snek game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off screen updates



#snek head
head = turtle.Turtle()
head.speed(0) #animation of turtle modu
head.shape("square")
head.color("lime")
head.penup() #not draw anything
head.goto(0,0) #head starts at middle of screen, does it anyways but 
head.direction = "stop" 


#snek food
food = turtle.Turtle()
food.speed(0) #animation of turtle modu
food.shape("circle")
food.color("red")
food.penup() #not draw anything
food.goto(0,100) 



#snek body
segments=[]

#objective
marker=turtle.Turtle()
marker.speed(0)
marker.shape("square")
marker.color("orange")
marker.penup()
marker.hideturtle()
marker.goto(0,245)
marker.write("Objective: Get Food!!", align="center",font=("Courier", 15, "normal") )

#rules
crayon=turtle.Turtle()
crayon.speed(0)
crayon.shape("square")
crayon.color("orange")
crayon.penup()
crayon.hideturtle()
crayon.goto(0,230)
crayon.write("Don't eat urself or cross the boundary~", align="center",font=("Courier", 15, "normal"))

#gameover

gameover=turtle.Turtle()
gameover.speed(0)
gameover.shape("square")
gameover.color("purple")
gameover.penup()
gameover.hideturtle()
gameover.goto(0,30)

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white") #text color
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


#functions


def go_up():
    if head.direction !="down": #no reverse direction
        head.direction ="up"
        gameover.clear()

def go_down():
    if head.direction !="up":
        head.direction ="down"
        gameover.clear()

def go_left():
    if head.direction !="right":
        head.direction ="left"
        gameover.clear()

def go_right():
    if head.direction !="left":
        head.direction ="right"
        gameover.clear()

def move():
    if head.direction =="up": # if head is up, will move 20
        y =head.ycor()
        head.sety(y + 20)
    if head.direction =="down": 
        y =head.ycor()
        head.sety(y - 20)
    if head.direction =="left": 
        x =head.xcor()
        head.setx(x - 20)
    if head.direction =="right": 
        x =head.xcor()
        head.setx(x + 20)

#keybinds (wn=window)
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")


#main game loop
while True:
    wn.update() #everytime loop -updates

    #checking collision w border - die
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
       
        gameover.write("Game Over", align="center",font=("Courier", 30, "normal", "italic", "bold"))
     
        #time.sleep(1)
       
   
        head.goto(0,0)
        head.direction = "stop"
        

        #hide segments
        for segment in segments:
            segment.goto(1000,1000)
        
        food.clear() 
    
        # clear segments lists
        segments.clear()

        #reset score
        score=0
        
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

       
        
   
       
        #reset delay/speed
        delay = 0.1
        

#check collision of food - score! 
    if head.distance(food) < 20:
        # move food to random spot
        x = random.randint(-290,290) #rando int range
        y = random.randint(-290,290)
        food.goto(x,y)


        #add segment - big back
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

      

        #shorten delay -faster hehe
        delay -= 0.001

        #increase score
        score += 10 # score = score+10

        if score> high_score:  #setting high score
            high_score = score 
        
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) #drawing over itself w/o clear
       
   
        


#move end segments first in reverse order - be big
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
#move segment 0 to head -be big
    if len(segments) > 0:
        x = head.xcor()
        y= head.ycor()
        segments[0].goto(x,y)



    move() 
    #check for head collision with body -die
    for segment in segments:
        if segment.distance(head) <20: #overlapping
            
            gameover.write("Game Over", align="center",font=("Courier", 30, "normal", "italic", "bold"))
            
            head.goto(0,0) #respawn
            head.direction="stop"

            #hide segments
            for segment in segments:
                segment.goto(1000,1000)
        
            # clear segments lists
            segments.clear() #lose points :/
            
            #reset score
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

            #reset delay/speed
            delay = 0.1

    time.sleep(delay) #stops program for 0.1sec

wn.mainloop()
