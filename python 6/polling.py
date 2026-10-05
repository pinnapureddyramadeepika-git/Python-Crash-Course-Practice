favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
#list of people who should take the poll
people_to_take_poll=['jen','vennala','mamatha','pushpa','edward','divya','phil']
#looping through the list to know who should take the poll
for person in people_to_take_poll:
    if person in favorite_languages:
     print(f"Thank you {person.title()} for respondng.")
    else:
       print(f"please take the poll {person.title()}.") 