
''' Breakfast subtracts one meal, since flights from the US don't arrive in the morning.'''
''' Dinners subtracts one meal, since flights to the US leave before dinner.'''

def meals():
    breakfast = (750 * days) - 750 
    breakfast = breakfast - 750
    lunch = 1500 * days
    dinner = 2000 * days
    dinner = dinner - 2000
    meal_cost = breakfast + lunch + dinner
    return meal_cost

def accomodation(acc_var):
	if acc_var == "1":
		return 8500 * days
	elif acc_var == "2":
		return 4500 * days
	elif acc_var == "3": 
		return 3000 * days
	else:
		print ("\nSorry, I wasn't clear. If you want to stay in a hotel, press 1; if you want to stay in a guest house, press 2; and if you want to stay in a hostel, press 3.")
		acc_error()

def acc_error():
	acc_var = raw_input("\nSo, then, what kind of place do you want to stay?")
	accomodation(acc_var)

days = int(raw_input("How many days do you want to stay in Japan?"))
print "\nOkay, %s days! Let's see..." % (days)
print "\nThat'll be about %s yen in meals..." % (meals())
acc_var = raw_input("\nWhat kind of place do you want to stay? A hotel (1), a guest house (2), or a hostel (3)?")
print "\nSo you'll spend about %s on accommodations..." % (accomodation(acc_var))


