#creating a list of my pizzas
My_pizzas = ['cheese volcano pizza','margherita','peppy panner','chicken golden delight','chicken sausage']
print(My_pizzas)
#making a copy of My_pizzas to Friend_pizzas
friend_pizzas= My_pizzas[:]
print(friend_pizzas)
#adding a new pizza to the orignal list
My_pizzas.append('mixed veggies pizza')
#adding a different pizza to the friend list
friend_pizzas.append('chillies pizza')
#printing the original list after adding 
print('My favourite pizzas are:')
for pizza in My_pizzas[:]:
 print(pizza)
#printing the friends list after addding to show difference netween two lists after adding
print("\nMy friend's favourite Pizzas are:") 
for pizza in friend_pizzas[:]:
 print(pizza)