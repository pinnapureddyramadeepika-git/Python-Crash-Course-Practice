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
#creating three different instances
#instance 1
hotel = Restaurant("Ranjith Daba","north india")
#instance 2
tiffin_centre = Restaurant("Swathi Tiffin Centre","breakfast")
#instance 3
cafe = Restaurant("Deeps Cafe",'desserts')
#calling describe method for each instance
hotel.describe_restaurant()
tiffin_centre.describe_restaurant()
cafe.describe_restaurant()
