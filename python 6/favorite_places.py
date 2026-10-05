#creating dictionary called favourite places
favourite_places = {
    'Deepika':['mypadu_beach','jyothi','tirumala'],
    'Dasa':['kadapa','pondicherry','gobi_place'],
    'mom':['temples','home','peddamma_house']
  }
for name,places in favourite_places.items():
    print(f"\n {name}'s favorite places are: ")
    for place in places:
        print(f'-{place}')