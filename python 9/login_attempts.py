#making the class User
class User:
#creating two attributes called first_name and last_name
    def __init__(self,first_name,last_name,age,course):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.course = course
        self.login_attempts = 0
#making the method called describe user
    def describe_user(self):
      print(f"The user's first name is {self.first_name}.")
      print(f"The user's last name is {self.last_name}.")
      print(f"The user {self.first_name}{self.last_name}'s  age is {self.age}.")
      print(f"The user {self.first_name}'s course is {self.course}.")
#making the method called greet user       
    def greet_user(self):
      print(f"Hello {self.first_name}! welcome to the new era.")
#making the method called increment login attempts
    def increment_login_attempts(self):
       self.login_attempts += 1
#making the method called reset login attempts
    def reset_login_attempts(self):
       self.login_attempts = 0       
#creating an instance
user_1 = User("rama","deepika",20,"CSM")
#calling increment login attempts several attempts
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
#Printing the value of login_attempts to make sure it was incremented properly
print(f" The login attempts made by user 1 is {user_1.login_attempts}.")
#calling the reset login attempts
user_1.reset_login_attempts()
 #printing the reset login pins to see
print(f"The reset login pins made by user 1 are {user_1.login_attempts}.")
#calling login attempts again to make sure it was reset to 0
user_1.increment_login_attempts()
 #printing login attempts again to make sure it was reset to 0
print(f"The login attempts after reset are {user_1.login_attempts}.")