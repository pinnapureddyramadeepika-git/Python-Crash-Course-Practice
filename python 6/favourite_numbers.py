#storing people's fav numbers in a list with in a dictionary 
fav_numbs={'Deepika':[6,7],
           'Dasa':[7,8],
           'Sujatha':[3,4],
           'Prabhakar':[8,9],
           }
#printing the person's name along with their favourite numbers 
for name, numbers in fav_numbs.items():
    print(f"{name}'s favourite nummber is :")
    for number in numbers:
            print(f"-{number}")