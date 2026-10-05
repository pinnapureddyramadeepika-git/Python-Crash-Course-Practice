#defining a function using paraameters like size and text 
def make_shirt(size,text):
#printing the imformation in  a sentence    
    print(f"The size of the shirt is {size} and message to be printed on it is '{text.title()}'.")
#calling the function using positional arguments
make_shirt(40,'I love myself')
#xalling the function using keyword arguments
make_shirt(size=35,text='Sayonara')