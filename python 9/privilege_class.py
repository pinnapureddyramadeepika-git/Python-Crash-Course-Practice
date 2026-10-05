from user_class import User
class Privilege:
   def __init__(self):
      self.privileges = ["can add post","can delete post","can ban user"]
   def show_privileges(self):
      for privilege in self.privileges:
         print(f"The privileges the users has are: {privilege}.")
class Admin(User):
   def __init__(self,first_name,last_name,age,course):
      super().__init__(first_name,last_name,age,course)
      self.privileges = Privilege()         