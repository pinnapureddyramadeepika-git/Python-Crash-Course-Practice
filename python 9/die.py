import random
class Die:
    def __init__(self,sides=6):
        self.sides = sides
    def roll_die(self):
     return random.randint(1,self.sides)
#6 sided die
six_die = Die()
print("The Result for rolling a 6 sided die: ")
for _ in range(10):
    print(six_die.roll_die())
#10 sided die    
ten_die = Die(10)
print("The Result after rolling a 10 sided die:")
for _ in range(10):
   print(ten_die.roll_die())
#20 sided die
twenty_die = Die(20)
print("The Result after rolling a 20 sided die: ")
for _ in range(20):
   print(twenty_die.roll_die())