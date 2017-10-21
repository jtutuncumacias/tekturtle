import turtle

#Dictionaries visualization lab (using turtle)

#   TODO:
#   add gridlines

sally = turtle.Turtle()
sally.shape("turtle")
sally.color("blue")
sally.setpos(100, 0)

alex = turtle.Turtle()
alex.shape("turtle")
alex.color("green")
alex.setpos(160, 80)

addressbook = {'sally': 5, 'carly': 2}

bob = turtle.Turtle()
bob.shape("turtle")
for num in range(addressbook['sally']):    #bob moves forward the number of steps it takes to get to sally
    bob.forward(20)

# with lists (turtle goes in 2+ directions)

bob.setpos(0, 0)

alex_address = [8, 4]
dave_address = [2, 2]

addressbook2 = {'alex': alex_address,
                'dave': dave_address}

for num in range((addressbook2['alex'])[0]):
    bob.forward(20)

bob.left(90)

for num in range((addressbook2['alex'])[1]):
    bob.forward(20)

