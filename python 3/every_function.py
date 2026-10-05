#CREATING A LIST
Hobbies = [ 'singing','vlogging','dancing','exercising','watching','dressing']
print( Hobbies )
#ACCESING ELEMENTS IN A LIST
print(Hobbies[0])
print(Hobbies[1])
print(Hobbies[2])
print(Hobbies[3])
print(Hobbies[4])
print(Hobbies[5])
#USING INDIVIDUAL VALUES FROM A LIST
msg = f"My favorite hobby is {Hobbies[2].upper()}"
print(msg)
msg =f"My personality wants to do {Hobbies[1].format()}"
print(msg)
#MODYFYING ELEMENTS IN A LIST
Hobbies[4]='exploring'
print(Hobbies)
#ADDING ELEMENT TO THE LIST
#1.APPENDING(ADDS ELEMENT TO THE END OF LIST)
Hobbies.append('experiencing')
print(Hobbies)
#2.INSERTING ELEMENTS IN A LIST(U CAN INSERT ANYWHERE TO THE LIST BY MENTIONING INDEX)
Hobbies.insert(5,'eating')
print(Hobbies)
#REMOVING ELEMENTS FROM A LIST
#1.REMOVING AN ITEM USING THE DEL STATEMENT
del Hobbies[5]
print(Hobbies)
#2.REMOVING AN ITEM USING POP() METHOD
popped_Hobby=Hobbies.pop()
print(Hobbies)
print(popped_Hobby)
everyday_hobby=Hobbies.pop()
print(f"everyday {everyday_hobby.title()} is done")
#3.POPPING AN ITEM FROM ANY POSITION IN A LIST(INCLUDES INDEX OF THE ITEM WE WANT TO REMOVE)
mostloved_hobby=Hobbies.pop(2)
print(f"my most lovable hobby is {mostloved_hobby.title()}")
#4.REMOVING AN ITEM BY VALUE
Hobbies.remove("exercising")
print(Hobbies)
#ORGANISING A LIST 
#1.SORTING A LIST PERMANENTLY WITH THE SORT()METHOD
# (PRINTS IN ALPHABETICAL ORDER)
Hobbies.sort()
print(Hobbies)
#(PRINTS IN REVERSE ALPHABETICAL ORDER)
Hobbies.sort(reverse=True)
print(Hobbies)
#2.SORTING A LIST PERMANENTLY WITH THE SORTED() FUNCTION
print("here is the original list:")
print(Hobbies)
print("\n here is the sorted list:")
print(sorted(Hobbies))
print("here is the original list again:")
print(Hobbies)
#PRINTING A LIST IN REVERSE ORDER
Hobbies.reverse()
print(Hobbies)
#finding the length of the list
list_length=len(Hobbies)
print(f'the length of the list is:{list_length}')