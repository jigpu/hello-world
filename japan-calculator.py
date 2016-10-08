####################### ACCOMODATION #######################
# This section doesn't work right with exception output

def accomodation(acc_var):
	if acc_var == "1":
		return 8500 * days
	elif acc_var == "2":
		return 4500 * days
	elif acc_var == "3": 
		return 3000 * days
	else:
		print "\nSorry, that's not a valid answer."
		return acc_error(acc_var)

def acc_error(acc_var):
	acc_var = raw_input("\nOnce again, press 1 for hotels, 2 for guest houses, and 3 for hostels.")
	accomodation(acc_var)
	

days = int(raw_input("How many days do you want to stay in Japan?"))
acc_var = raw_input("\nWhat kind of accomodations do you want?\n     If you want to stay in a hotel, press 1.\n     If you want to stay in a guest house, press 2.\n     If you want to stay in a hostel, press 3. \n")
print "\nSo you'll spend about %s on accommodations..." % (accomodation(acc_var))
