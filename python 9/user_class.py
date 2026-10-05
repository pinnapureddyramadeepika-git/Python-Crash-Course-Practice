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