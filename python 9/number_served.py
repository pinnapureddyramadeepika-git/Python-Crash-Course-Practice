class Restaurant:#the class name should always be started with capital letter
#using __init__ method to store attributes
 def __init__(self,restaurant_name,cuisine_type):
  self.restaurant_name = restaurant_name
  self.cuisine_type = cuisine_type
  self.number_served = 0 
#making the method called describe_restaurant()
 def describe_restaurant(self):
     print(f"The restaurant name is {self.restaurant_name}.")
     print(f"The {self.restaurant_name} serves {self.cuisine_type} cuisine.")
#making another method called open_restaurant()  
 def open_restaurant(self): 
    print(f"The {self.restaurant_name} is now open.")
#adding a method called set number served    
 def set_number_served(self,number):
  self.number_served = number  
#adding a method called increment number served
 def increment_number_served(self,increment):
   self.increment_number_served = increment   
#making an instance restaurant from class Restaurant
restaurant = Restaurant("Andhra spice","south india")
#printing the number of customers the restaurant has served
print(f"The {restaurant.restaurant_name} has served {restaurant.number_served} customers.")
#changing the default value from 0 to 6 and printing it again
restaurant.number_served = 6
print(f"The {restaurant.restaurant_name} has served {restaurant.number_served} customers as of now.")
#calling the method called set number served with a new number
restaurant.set_number_served(9)  
print(f"The {restaurant.restaurant_name} has served {restaurant.number_served} customers.")
#calling the method increment number served 
restaurant.increment_number_served(12)
print(f"The {restaurant.restaurant_name} served {restaurant.increment_number_served} customers, say, a day of business")