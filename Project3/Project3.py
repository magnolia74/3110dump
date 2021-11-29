# You may run the code you want or edit your way.
legal_input = False



while (not legal_input): 
	three_int = float(input("Enter three sides of a triangle: "))
	side_str = three_int.split()
	side = sorted( [int(side_str[0]), int(side_str[1]), int(side_str[2])] )

	
	if (side[0] > 0):
		legal_input = (side[0] + side[1] > side[2]) 
		if (not legal_input): 
			print ("The two short sides won't stretch to span the long one")

	else: 
		print("All sides must be positive")
def FindLengthofC(): 
    side[0]^2+side[1]^2=side[2]^2	
    return FindLengthofC
def FindAngle():
    side[2]^2=side[0]^2+side[1]^2-2(side[0])(side[1])*cos(side[2])
    return FindAngle 
def TriangleChecker(): 
    if (side[0] == side[2]): 	
	    print("Triangle is equilateral")
    elif (side[0] == side[1]  or  side[1] == side[2]): 
	    print("Triangle is isosceles")
    else: 
	    print("Triangle is scalene")
	
    # Determine [ right | obtuse ] triangle

    pyth_diff = side[2]**2 - (side[0]**2 + side[1]**2) 
        if (pyth_diff > 0): 
	        print ("Triangle is obtuse")
        elif (pyth_diff == 0): 
	        print ("Triangle is right")
	