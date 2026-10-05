guests = ('jeja','abba','lohi','haritha')
message = 'sorry guys, I can only invite two people to dinner'
print(f"{guests[0]},",message)
print(f"{guests[1]},",message)
guest_not = guests.pop(0)
del guests[0,1]
print(guests)
print( f'The guests who is not coming is {guest_not.title()}')
len(guests)
print("The number of guests coming are : ", len(guests))
