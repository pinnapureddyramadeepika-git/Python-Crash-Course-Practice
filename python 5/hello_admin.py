#creating a list 
usernames =['deepikareddy.6','harithareddy_200','lohi_reddy','dasaradha_07','deepsoulscope','admin']
for username in usernames:
#special case of admin 
 if username == 'admin':
    print(f"\nHello admin, would you like to see a status report?")
 else:
    print(f"\nHello {username}, thank you for logging in again.")   