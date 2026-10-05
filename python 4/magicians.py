#creting a list
magicians = ['alice','david','carolina']
#using FOR loop
for magician in magicians : # add : tells python to interpret the next line as the  start of the loop
 #printing the names of magician with a line 
 #here we gave indentation (means leaving space before print)
 print (f'{magician.title()},that was a great trick!')
 #adding another line
 #\n creates a set of messages that are neatly grouped for each person in the list
 print(f"I can't wait to see another trick {magician.title()}. \n")
 #doing something after the loop
print(f'thank you every one!, that was a great magicshow')#this line is printed at the end as it is not indented 
#we should not indent unnecessarily after the loop as we dont want the line to print for everyone 