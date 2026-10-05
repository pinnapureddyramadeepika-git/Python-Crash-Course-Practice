#creating a dictionary of rivers along with thier country
rivers={
    'nile':"egypt",
    'ganga':"india",
    'chenab':"pakisthan"
}
for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")
print("---Rivers---")    
for river in rivers.keys():
    print(f'{river.title()}')
print("---Countries---")    
for country in rivers.values():
    print(f'{country.title()}')