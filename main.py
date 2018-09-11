import common
import student_code

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"

	
policy_value={}
policy_value['s'] = common.constants.SOFF
policy_value['w'] = common.constants.WOFF
policy_value['n'] = common.constants.NOFF
policy_value['e'] = common.constants.EOFF
policy_value['S'] = common.constants.SON
policy_value['W'] = common.constants.WON
policy_value['N'] = common.constants.NON
policy_value['E'] = common.constants.EON
policy_value['X'] = common.constants.EXIT
	
def set_policies(map,data):
	for y in range(6):
		for x in range(6):
			map[y][x]=policy_value[data[y*6+x]]

def set_values(map, data):
	for y in range(6):
		for x in range(6):
			map[y][x]=data[y*6+x]

def init_map():
	return [[0 for x in range(6)] for x in range(6)]

def set_map(map, data):
	for y in range(6):
		for x in range(6):
			map[y][x]=int(data[y*6+x])

def check_policies(map, map_gold, show):
	s="XswneSWNE";
	result=True;
	for y in range(6):
		v=""
		for x in range(6):
			value = map[y][x]
			if (map_gold[y][x]==value):
				v+=bcolors.GREEN
			else:
				result = False
				v+=bcolors.RED
			v+=s[value]
		v+=bcolors.NORMAL
		if (show):
			print v;
	return result;

def withinprc(value, ref, prc):
	margin = ref*prc
	if margin < 0:
		margin = -margin
	return ref-margin<=value and ref+margin>=value
	
def check_values(map, map_gold,  show):
	result=True;
	for y in range(6):
		v=""
		for x in range(6):
			value = map[y][x]
			if withinprc(value,map_gold[y*6+x],.01):
				v+=bcolors.GREEN
			else:
				result = False
				v+=bcolors.RED
			v+="{0:.2f}\t".format(value+0)
		v+=bcolors.NORMAL
		if (show):
			print v;
	return result;

def run_experiment(data, value_gold, p_gold, values_gold, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle):
	result=True

	map = init_map()
	set_map(map, data)

	pp = init_map()

	vv = common.init_values()
	
	
	value = student_code.drone_flight_planner (map, pp, vv, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle)

	pp_gold = init_map();
	set_policies(pp_gold, p_gold)
	

	if (not check_policies(pp,pp_gold,False)):
		print "Policies results: "+bcolors.RED+"FAIL"+bcolors.NORMAL
		check_policies(pp,pp_gold,True)
		result=False
	else:
		print "Policies results: "+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL
	

	if (not check_values(vv,values_gold,False)):
		print "Values results: "+bcolors.RED+"FAIL"+bcolors.NORMAL
		check_values(vv,values_gold,True)
		result=False
	else:
		print "Values results: "+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL
	
	if withinprc ( value,value_gold,.01):
		print ("Delivery job value: {0:.2f} ("+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL+")").format(value)
	else:
		print ("Delivery job value: {0:.2f} ("+bcolors.RED+"FAIL"+bcolors.NORMAL+") - correct value ({1:.2f})").format(value,value_gold)
		result=False
	return result

all_passed=True

			
data1 = ("000000"
"010030"
"000000"
"000000"
"003000"
"000020")
			   
p_gold1 = ("ssssns"
"esSwXS"
"eEEsSs"
"eeneSs"
"swXeSs"
"eEEEXW")
				 
values_gold1 = [38.73, 42.33, 45.72, 42.87, 32.49, 40.52,
						 42.38, 47.06, 52.00, 49.21,-100.00,46.80,
						 46.05, 52.05, 59.02, 66.80, 72.33, 70.86,
						 44.93, 49.73, 55.85, 73.82, 80.60, 77.37,
						 44.15, 43.34,-100.00,82.10, 89.78, 84.00,
						 49.14, 55.41, 63.20, 90.39, 100.00,90.59]

print("Map1:");
all_passed = run_experiment(data1, 46.68, p_gold1, values_gold1, 100, 1, 100, .05) and all_passed
print
						 

						 

data2 = ("000000"
"000010"
"000300"
"000000"
"020030"
"000000")
			   
p_gold2 = ("sswwww"
"sswnww"
"sswXen"
"sswsWw"
"eXwwXe"
"nnwwWw")
				 
values_gold2 = [  4.25, 4.44,-1.38,  -9.08, -16.31,-22.89,
	                         12.05,13.58, 6.06, -13.12, -20.68,-26.55,
							 20.14,24.06,15.62,-200.00, -32.50,-31.82,
							 28.33,36.04,26.33,  10.90, -23.80,-30.81,
							 36.33,50.00,36.04,  23.37,-200.00,-38.24,
							 28.38,36.33,28.33,  20.03, -15.23,-23.99]

print("Map2:");
all_passed = run_experiment(data2, -20.683084, p_gold2, values_gold2, 50, 5, 200, .05) and all_passed
print


						 

data3 = ("203000"
"003000"
"003000"
"003000"
"000000"
"000001")
			   
p_gold3 = ("XWXeSS"
"NWXESS"
"NWXESS"
"NWXeSS"
"NWsWWW"
"NwWWWW")
				 
values_gold3 = [  200.00,196.92,-500.00,159.76,161.72,161.35,
	                         196.92,194.19,-500.00,162.05,164.30,163.59,
							 193.89,191.22,-500.00,164.74,167.00,165.82,
							 190.90,188.27,-500.00,168.04,169.79,168.02,
							 187.95,185.40,178.24,175.16,172.62,170.18,
							 185.08,182.85,180.09,177.33,174.62,171.97]

print("Map3:");
all_passed = run_experiment(data3, 171.97, p_gold3, values_gold3, 200, .1, 500, .01) and all_passed
print


						 
data4 = ("000000"
"000000"
"000000"
"003000"
"100002"
"003000")
			   
p_gold4 = ("eeeesS"
"eeeesS"
"eeEesS"
"sSXEES"
"EEEEEX"
"nNXeeN")
				 
values_gold4 = [  2118.28,2571.48,3076.57,3631.31,4230.25,4816.32,
	                         2313.14,2859.95,3507.49,4266.84,5063.20,5836.30,
							 2410.35,2985.84,3733.60,5087.40,6030.60,7021.31,
							 2348.09,2574.66,-500.00,6015.52,7136.40,8398.10,
							 2830.99,3622.68,4665.61,6882.79,8300.06,10000.00,
							 2348.09,2574.66,-500.00,6281.71,7308.73,8415.15]

print("Map4:");
all_passed = run_experiment(data4, 2830.98, p_gold4, values_gold4, 10000, 100, 500, .10) and all_passed
print


data5 = ("000000"
                   "000000"
                   "000000"
                   "003000"
                   "100002"
                   "003000")
			   
p_gold5= ("EEEESS"
                     "EEEESS"
                     "EEnESS"
                     "NwXEES"
                     "NWEEEX"
                     "NWXEEN")
				 
values_gold5 = [  8942.09,9051.30,9159.50,9265.89,9369.73,9458.43,
	                         8973.70,9101.96,9235.63,9373.09,9490.18,9589.20,
							 8887.70,9004.64,9146.99,9492.33,9612.52,9722.90,
							 8766.02,8680.07,-500.00,9610.81,9735.37,9859.71,
							 8643.62,8539.54,7587.67,9705.65,9848.88,10000.00,
							 8524.10,8430.97,-500.00,9636.97,9750.31,9861.36]

print("Map5");
all_passed = run_experiment(data5, 8643.62, p_gold5, values_gold5, 10000, .1, 500, .01) and all_passed
print


data6 = ("000000"
                   "000000"
                   "000000"
                   "003000"
                   "100002"
                   "003000")
			   
p_gold6= ("ssssss"
                     "ssssss"
                     "esssss"
                     "eeXwss"
                     "eeseeX"
                     "eeXwen")
				 
values_gold6 = [  -26070.68,-23496.14,-20933.07,-21617.33,-20863.11,-18937.84,
	                         -22824.06,-19286.73,-15623.42,-17420.39,-16489.15,-13594.78,
							 -19268.41,-14438.60,-8996.75,-12833.64,-11590.64,-7195.96,
							 -15487.75,-8925.09,-500.00,-8022.77,-6169.28,540.05,
							 -16768.20,-12302.80,-7951.10,-7223.90,-252.56,10000.00,
							 	-14270.99,-8064.60,-500.00,-7271.94,-5331.16,670.86]

