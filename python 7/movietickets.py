#charging different ticket prices based on their age
active = True
while active:
 age = input("your age please..(or quit to stop)?")
 if age.lower() =='quit':
    break
 age = int(age)
 if age < 3:
    print("The movie ticket is free for you.")
 elif age <= 12: 
    print("The movie ticket is 10$ for you.")
 else:
    print("The movie ticket price is 15$ for you.")       