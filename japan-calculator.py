''' JAPAN TRIP CALCULATOR '''

# Need to define costs per day for food, hotels (maybe with a fanciness scale?), 
# plane ride (maybe with a time of year calculator?), trains, spending money

################################################################################
# First, caluclate the total (in yen) of each meal. Note that breakfast
# substracts one day because flights from the States don't land in Japan in the
# morning.

def breakfast(days):
    days = days - 1
    return 750 * days
    
def lunch(days):
    return 1500 * days

def dinner(days):
    return 2000 * days    

# Then return the total value of all meals for the trip. #
def food(days):
    return breakfast(days) + lunch(days) + dinner(days)

################################################################################
# Next, calculate the total (in yen) of the hotel stay.

def trip_length(days):
	days = days * 1
	return days
	
def accomodation(ac_type):
	if ac_type == "hostel":
		return 3500
	elif ac_type == "guest-house":
		return 4500
	elif ac_type == "hotel":
		return 7500
	else:
		return "Sorry, try again"
		
def trip_cost(ac_type, days):
	return accomodation(ac_type) * trip_length(days)

################################################################################
# Print the food cost and the accomodation cost side by side.

print food(2)
print trip_cost("guest-house", 2)
print "\nTOTAL"
print food(2) + trip_cost("guest-house", 2)
