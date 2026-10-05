#creating a dictionary called cities
cities= {
    "Kadapa":{
        "country":"India",
        "population":"6 lakh",
        "fact":"factionist city of ANDHRAPRADESH"
    },
    "Hyderabad":{
        "country":"India",
        "population":"8 lakh",
        "fact":"IT hub of India"
    },
    "Banglore":{
        "country":"India",
        "population":"9 lakh",
        "fact":"Silicone valley of India"
    }
}
for city,info in cities.items():
    print(f"\ncity:{city}")
    for key, value in info.items():
        print(f'{key.title()}:{value}')