#creating dictionariies about pets 
pet_1 = {'animal':'Dog','owner':'Deepika'}
pet_2 = {'animal':'cat','owner':'Nannamma'}
pet_3 = {'animal':'fish','owner':'nature'}
pet_4 = {'animal':'hedgehog','owner':'stranger'}
#storirng them in a list
pets = [pet_1, pet_2, pet_3, pet_4]
#using for loop to print each dictionary
for  pet in pets:
    print(f"{pet['owner']}'s pet animal is {pet['animal']}.")