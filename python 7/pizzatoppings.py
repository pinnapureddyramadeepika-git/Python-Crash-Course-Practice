#writing a loop that prints the user's liked toppings to their pizza and 
# printing the message back to them 
prompt = "\nEnter the toppings you want to add to the pizza (or quit to end): "
while True:
    topping = input(prompt)    
    if topping =='quit':
         break
    else:
      print(f"Adding {topping} to your pizza.")  


