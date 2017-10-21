import turtle

#Dictionaries visualization lab (using turtle)

addressbook = {'sally': 5, 'alex': 8, 'carly': 2}

bob = turtle.Turtle()
turtle.Screen().bgcolor("black")
turtle.color("white")
turtle.shape("turtle")
for num in range(addressbook['sally']):    #bob moves forward the number of steps it takes to get to sally
    bob.forward(20)

sally_address = [5, 3]
alex_address = [8, 4]
carly_address = [2, 2]

addressbook2 = {'sally': sally_address,
                'alex': alex_address,
                'carly': carly_address}

for num in range((addressbook2['alex'])[0]):
    bob.forward(20)

bob.left(90)

for num in range((addressbook2['alex'])[1]):
    bob.forward(20)

