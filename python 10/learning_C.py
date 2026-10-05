with open ('learning_python.txt') as file_object:
    for line in file_object:
        modified_line = line.replace('Python',"C")
        print(modified_line)
