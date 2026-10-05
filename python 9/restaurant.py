class Restaurant:#the class name should always be started with capital letter
#using __init__ method to store attributes
 def __init__(self,restaurant_name,cuisine_type):
  self.restaurant_name = restaurant_name
  self.cuisine_type = cuisine_type
#making the method called describe_restaurant()
 def describe_restaurant(self):
     print(f"The restaurant name is {self.restaurant_name}.")
     print(f"The {self.restaurant_name} serves {self.cuisine_type} cuisine.")
#making another method called open_restaurant()  
 def open_restaurant(self): 
    print(f"The {self.restaurant_name} is now open.")
#making an instance restaurant from class Restaurant
restaurant = Restaurant("Andhra spice","south india")
print(f"The restaurant name is {restaurant.restaurant_name}.")
print(f"It serves {restaurant.cuisine_type}.")
#calling the both methods
restaurant.describe_restaurant() 
restaurant.open_restaurant() 