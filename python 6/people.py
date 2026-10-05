#creating 3 dictionaries 
me ={'first_name':"RamaDeepika",'last_name':"Pinnapureddy",'age':20,
              'city':'Kadapa'}
thambi = {'first_name':"DasaRadha",'last_name':"Pinnapureddy",'age':18,
          'city':'kadapa'}
kodalu ={'first_name':"Brahmini",'last_name':"Arava",'age':0.9,
         'city':"Badvel" }
#stored them in s lidt called people
people  = [me , thambi, kodalu]
#looping through the list of people and printing them
for person in people:
    print(f'{person['first_name']} {person['last_name']} is {person['age']} years old and lives in {person['city']}.')
