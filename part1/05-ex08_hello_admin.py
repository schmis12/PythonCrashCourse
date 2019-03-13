# Stefan J. Schmidt, 13.03.2019

usernames = ['damla', 'victoria', 'admin', 'diana', 'artur']

for username in usernames:
	if username == 'admin':
		print(f'Hello {username.title()}, would you like to see a status report?')
	else:
		print(f'Hello {username.title()}, thank you for logging in again.')