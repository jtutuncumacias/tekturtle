import turtle

#Dictionaries visualization lab (using turtle)


#----------STARTER CODE BEGINS----------#

grid = turtle.Turtle()
grid.color("gray")
grid.hideturtle()
grid.speed(0)
for num in range(-10, 11):
    grid.penup()
    grid.goto(-200, num * 20)
    grid.pendown()
    grid.goto(200, num * 20)
for num in range(-10, 11):
    grid.penup()
    grid.goto(num * 20, -200)
    grid.pendown()
    grid.goto(num * 20, 200)

bob = turtle.Turtle()       # our main character bob
bob.shape("turtle")

sally = turtle.Turtle()
sally.shape("turtle")
sally.color("blue")
sally.penup()
sally.goto(100, 0)        #sally lives at the coordinates (100, 0)

alex = turtle.Turtle()
alex.shape("turtle")
alex.color("green")
alex.penup()
alex.goto(160, 80)        #alex lives at (160, 80)

#----------STARTER CODE ENDS----------#


# Exercise 1: get bob to where sally lives

addressbook = {'sally': 5, 'carly': 2}

for num in range(addressbook['sally']):    #bob moves forward the number of steps it takes to get to sally
    bob.forward(20)

# Exercise 2: with lists (turtle goes in 2+ directions)
# get bob to where alex lives

bob.goto(0, 0)    #bob goes back to his original position

alex_address = [8, 4]
dave_address = [2, 2]

addressbook2 = {'alex': alex_address,
                'dave': dave_address}


for num in range((addressbook2['alex'])[0]):
    bob.forward(20)

bob.left(90)

for num in range((addressbook2['alex'])[1]):
    bob.forward(20)

