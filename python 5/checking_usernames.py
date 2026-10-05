#making a list of current users
current_users=['deepika','haritha','lohitha','brahmini','dasa','sujatha','prabhakar']
#making a list of new users
new_users=['deepika','damini','deepu','siddu','prabhakar']
# Make a lowercase copy of current_users for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]
# Loop through new_users and check availability
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry, the username '{user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{user}' is available!")
