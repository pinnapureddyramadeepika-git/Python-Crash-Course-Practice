from pathlib import Path
path = Path('learning_python.txt')
#printing the contents by reading the entire file
contents = path.read_text()
print(contents)
#printing the contents by storing the lines 
# in a list and then looping over each line
lines = contents.splitlines()
for line in lines:
    print(line)