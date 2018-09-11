import common


def find_starting_point(map):
	for row in range(6):
		for col in range(6):
			if map[row][col] == 1:
				return row, col

def find_ending_point(map):
	for row in range(6):
		for col in range(6):
			if map[row][col] == 2:
				return row, col

def find_next_block(row, col, direction):
	#dir = 1: south
	#dir = 2: west
	#dir = 3: north
	#dir = 4: east
	if direction == 1: 
		if row - 1 < 0:
			return row, col
		return row -1, col
	elif direction == 2:
		if col - 1 < 0:
			return row, col
		return row, col - 1
	elif direction == 3: 
		if row + 1 > 5:
			return row, col
		return row + 1, col
	else:
		if col + 1 > 5:
			return row, col
		return row, col + 1

def Copy_Values(valMap): return [row[:] for row in valMap]

def find_max(row, col, battery_drop_cost, gamma, ValCopy):
	southY, southX = find_next_block(row,col,1)
	westY, westX = find_next_block(row,col,2)
	northY, northX = find_next_block(row,col,3)
	eastY, eastX = find_next_block(row,col,4)
	#Now compute the values
	southOFF = gamma* (.15 * ValCopy[westY][westX] + .15*ValCopy[eastY][eastX] + .7*ValCopy[southY][southX]) - battery_drop_cost
	southON = gamma* (.1 * ValCopy[westY][westX] + .1*ValCopy[eastY][eastX] + .8*ValCopy[southY][southX]) - 2.0*battery_drop_cost
	westOFF = gamma* (.15 * ValCopy[southY][southX] + .15*ValCopy[northY][northX] + .7*ValCopy[westY][westX]) - battery_drop_cost
	westON = gamma* (.1 * ValCopy[southY][southX] + .1*ValCopy[northY][northX] + .8*ValCopy[westY][westX]) - 2.0*battery_drop_cost
	northOFF = gamma* (.15 * ValCopy[westY][westX] + .15*ValCopy[eastY][eastX] + .7*ValCopy[northY][northX]) - battery_drop_cost
	northON = gamma* (.1 * ValCopy[westY][westX] + .1*ValCopy[eastY][eastX] + .8*ValCopy[northY][northX]) - 2.0*battery_drop_cost
	eastOFF = gamma* (.15 * ValCopy[southY][southX] + .15*ValCopy[northY][northX] + .7*ValCopy[eastY][eastX]) - battery_drop_cost
	eastON = gamma* (.1 * ValCopy[southY][southX] + .1*ValCopy[northY][northX] + .8*ValCopy[eastY][eastX]) - 2.0*battery_drop_cost
	maxVal = southOFF
	maxPolicy = 3
	if southON > maxVal:
		maxVal = southON
		maxPolicy = 7
	if westOFF > maxVal:
		maxVal = westOFF
		maxPolicy = 2
	if westON > maxVal:
		maxVal = westON
		maxPolicy = 6
	if northOFF > maxVal:
		maxVal = northOFF
		maxPolicy = 1
	if northON > maxVal:
		maxVal = northON
		maxPolicy = 5
	if eastOFF > maxVal:
		maxVal = eastOFF
		maxPolicy = 4
	if eastON > maxVal:
		maxVal = eastON
		maxPolicy = 8
	return maxVal, maxPolicy

def drone_flight_planner(map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle):
	#Adjust Gamma
	gamma = 1 - discount_per_cycle
	#Fill in the rival shops
	for row in range(6):
		for col in range(6):
			if map[row][col] == 3:
				values[row][col] = -dronerepair_cost
	#Find the end and fill in
	finalRow, finalCol = find_ending_point(map)
	values[finalRow][finalCol] = delivery_fee
	
	for count in range(1000):
		#Make a copy of values chart
		ValCopy = Copy_Values(values)
		for row in range(6):
			for col in range(6):
				if map[row][col] == 2:
					continue
				if map[row][col] == 3:
					continue
				#Assign value
				maxVal, maxPolicy = find_max(row, col, battery_drop_cost, gamma, ValCopy)
				values[row][col] = maxVal
				policies[row][col] = maxPolicy
	#Return Optimal
	initRow, initCol = find_starting_point(map)
	return values[initRow][initCol]





















