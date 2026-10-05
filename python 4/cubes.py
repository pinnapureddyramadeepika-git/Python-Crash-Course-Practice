#cube: a number raised to third power is called cube
#creating a list of cubes from 1 to 10
cubes=[]
#using for loop to print the values
for value in range(1,11):
    cube=value**3
    cubes.append(cube)
    print(cube)