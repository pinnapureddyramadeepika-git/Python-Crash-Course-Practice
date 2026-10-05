#creating a tuple
basic_foods = ('alfaham mandi','dum biryani','veg biryani','chicken biyani','mutton biryani')
#using for loop to print each food
print('menu of the restaurant:\n')
for  food_item in basic_foods:
 print(food_item)
#trying to modify the tuple and pytho rejects it as we canat modify a tuple
#basic_foods[1] = 'mutton kheema'
#replacing the 2 items
basic_foods = ('gobi manchuria','prawns biryani')
print('\nnew menu of the restaurant:')
 #using for loop to print 
for food in basic_foods:
   print (food)