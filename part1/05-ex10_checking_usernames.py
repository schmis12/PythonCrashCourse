# Stefan J. Schmidt, 13.03.2019

current_users = ['damla', 'vicky', 'admin', 'diana', 'artur', 'ben']
new_users = ['alf', 'flash', 'ben', 'diana', 'hulk']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorry, user name '{new_user}' is already used." +
            ' Please choose a different one.')
    else:
        print(f"Fine, user name '{new_user}' is still available.")


