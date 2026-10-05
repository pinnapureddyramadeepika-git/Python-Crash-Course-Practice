import random
lottery = [6,4,2,8,9,6,4,2,3,1,'a','r','d','e','p','g']
winning_ticket = random.sample(lottery,4)
print("The winning ticket is: ",winning_ticket)
print("Any ticket with these 4 matching numbers or letters wins a prize")