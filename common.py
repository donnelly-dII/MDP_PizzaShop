class constants:
#MAP CONSTANTS
	EMPTY =1
	PIZZA =1
	CUSTOMER =2
	RIVAL =3
#DIRECTION CONSTANTS
	SOUTH =1
	WEST =2
	NORTH =3
	EAST =4
#ACTION CONSTANTS
	EXIT =0
	SOFF =1
	WOFF =2
	NOFF =3
	EOFF =4
	SON =5
	WON =6
	NON =7
	EON =8

class variables:
	explored=0
	
def print_map(map , V):
	s="XswneSWNE"
	print
	for y in range(6):
		v=""
		for x in range(6):
			v+=s[map[y][x]]
		v+='\t'		
		for x in range(6):
			v+="{0:.2f}".format(V[y][x])
			if v<5:
				v+=","
		print v
		
def init_values():
	return [[0 for x in range(6)] for x in range(6)]