#Items served at the OM NOM NOM place
#I've done a similar line for an RPG game before that I wanted randomized Item offers for an item shop a long time ago in Ruby. Feels similar

foods = ("Pepperoni Pizza", "Cesar Salad", "Roseta Cake", "Holy Tacos", "Coffee Icecream")
print("Original menu:")
for food in foods:
    print(food)

#Failure clause of the assignment
foods[1] = "Riggitoni Pasta"

#Revised Menu
foods = ("Pepperoni Pizza", "Cesar Salad", "A Soup Rock", "Unholy Burritos", "Coffee Icecream")
print("\nRevised menu:")
for food in foods:
    print(food)
