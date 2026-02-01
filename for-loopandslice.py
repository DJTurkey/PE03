#Animal list as per the assignment
#Defining the animals on list
animals = ["dog", "cat", "hawk", "otter", "elephant", "lizard", "dolphin"]
for animal in animals:
    print(animal)

#print from the beginning
print("\nThe first three animals in the list are:")
print(animals[:3])

#print from the middle
mid = len(animals) // 2
print("\nThree animals from the middle of the list are:")
print(animals[mid - 1: mid + 2])

#print from the end
print("\nThe last three animals in the list are:")
print(animals[-3:])