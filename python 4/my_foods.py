#creating a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
#using for loop to print
for food in my_foods[:]:
 print(food.title())
print("\nMy friend's favorite foods are:")
#using for loop to print
for food in friend_foods[:]:
 print(food.title())
