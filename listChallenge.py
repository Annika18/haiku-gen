#List Challenge

import random

#NAME GENERATOR
firstName = ["Joey", "Allison", "Nancy", "Rob", "Eddy", "Paisley", "Charlie", "Izzy"]
lastName = ["Brown", "Garcia", "May", "Zhang", "Simon"]

print (random.choice(firstName) + " " + random.choice(lastName))
print("---")

#MENU GENERATOR
appetizers = ["onion rings", "chips and dip", "boneless wings", "none"]
meal = ["burger with fries", "salmon and rice", "fish and chips", "garden salad"]
dessert = ["milkshake", "cheesecake", "key lime pie", "icecream sundae", "none"]

print("Your appetizer is: " + random.choice(appetizers))
print("Your main course is: " + random.choice(meal))
print("Your dessert is: " + random.choice(dessert))
print("---")

#HAIKU GENERATOR
fiveSyl = ["flowers are blooming", "the ocean is still", "I walk this old path", "children are laughing", "snow blankets our earth", "she sits in the dark", "wind catches the sail", "a barn cat cries out"]
sevenSyl = ["nothing matters anymore", "I feel calm and at home now", "rain washes away worries", "it is never quiet here", "flames jump higher in the dark", "blossoms fall and widows weep"]

line1 = random.choice(fiveSyl)
line2 = random.choice(sevenSyl)
line3 = random.choice(fiveSyl)
while line1 == line3:
    line3 = random.choice(fiveSyl)

print(line1)
print(line2)
print(line3)
