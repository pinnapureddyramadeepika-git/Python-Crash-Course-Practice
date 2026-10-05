filename = 'guest.txt'
name = input("May i know your name,please: ")
with open(filename, 'w') as file_object:
    file_object.write(name)
print(f"Welcome,{name}! your name has been saved.")
