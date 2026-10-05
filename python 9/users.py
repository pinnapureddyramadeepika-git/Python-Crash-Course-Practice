#making the class User
class User:
#creating two attributes called first_name and last_name
    def __init__(self,first_name,last_name,age,course):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.course = course
#making the method called describe user
    def describe_user(self):
      print(f"The user's first name is {self.first_name}.")
      print(f"The user's last name is {self.last_name}.")
      print(f"The user {self.first_name}{self.last_name}'s  age is {self.age}.")
      print(f"The user {self.first_name}'s course is {self.course}.")
#making the method called greet user       
    def greet_user(self):
      print(f"Hello {self.first_name}! welcome to the new era.")
#creating several instances
user_1 = User("rama","deepika",20,"CSM")
user_2 = User("dasa","radha",18,"CSM")
user_3 = User("prabhakar","reddy",51,"pharmacy")
#calling the both methods for user 1
user_1.describe_user()
user_1.greet_user()
#calling the both methods for user 2
user_2.describe_user()
user_2.greet_user()
#calling the both methods for user 3
user_3.describe_user()
user_3.greet_user()