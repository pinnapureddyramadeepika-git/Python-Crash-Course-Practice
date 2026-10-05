filename = 'guest_boook.txt'
print("enter 'quit' when you are finished.")
while True:
    name = input("May i know your name,please: ")
    if name.lower() == 'quit':
        break
    with open(filename, 'w') as file_object:
        file_object.write(name + "\n")
    print(f"Welcome,{name}! your name has been saved.")
