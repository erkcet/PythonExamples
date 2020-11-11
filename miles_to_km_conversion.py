####################################################
#   Converts Miles to KM
###################################################

def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km
my_trip_miles = 55
my_trip_km = convert_distance(my_trip_miles)
print("The distance in kilometers is " + str(my_trip_km))
