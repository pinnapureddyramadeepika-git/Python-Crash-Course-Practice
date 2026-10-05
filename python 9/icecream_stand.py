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
#creating class called iccream stand that inherits from class restaurant
class Icecream_stand(Restaurant):
  #representing aspects of restaurant
  def __init__(self,restaurant_name,cuisine_type="ice cream"):
    #initialising attributes of the parent class
    super().__init__(restaurant_name,cuisine_type)
    self.icecream_flavours = ["chocolate","vanilla","strawberry","pista"]
  def flavours_of_icecream(self):
   for icecream_flavour in self.icecream_flavours:
    print(f"The icecream stand has {icecream_flavour} flavours available now.")
#creating an instance
my_stand = Icecream_stand("flavours by deepika")
my_stand.describe_restaurant()
my_stand.flavours_of_icecream() 