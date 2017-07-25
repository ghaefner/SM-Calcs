import numpy as np

interaction = "v3sb90_12_new"
interaction_new = "v3sb90"

f = open("%s_m.int" % interaction_new ,"w")
f.write("! USDB Interaction copied from ANTOINE")
f.write("\n")
#f.write("! 1 = 0D5/2, 2 = 1S1/2, 3 = 0D3/2")
#f.write("\n")

#Function to converting strings to numbers: either ints or floats
def num(s):
	try:
		return int(s)
	except ValueError:
		return float(s)
		
		
with open("%s.int" % interaction,"r") as g:
	data = [x.split() for x in g.readlines()]
	
for i in range(1,len(data)):
	for j in range(len(data[i])):
		data[i][j] = num(data[i][j])
	
N_tbme = 0

for i in range(3,len(data)):
	for j in range(len(data[i])):
		if isinstance(data[i][j],float):
			N_tbme += 1

print(N_tbme)
	
#Single-particle states
sps = [[],[]]
for i in range(len(data[1])-2):
	sps[0].append(data[1][i+2])
	sps[1].append(data[2][i]+0.0001)

#print(sps)
	
f.write("+" + str(N_tbme))	
for i in range(len(sps[1])):
	f.write("      " + str(sps[1][i]))
f.write("\n")

#TBME
for i in range(4,len(data)):
	if isinstance(data[i][0],int):
		T_min = data[i][0]
		T_max = data[i][1]
		J_min = data[i][-2]
		J_max = data[i][-1]
		
		shells = []
		for j in range(2,6):
			shells.append(sps[0].index(data[i][j])+1)
			
			
		#Reihenfolge von sps checken
		if shells[0] > shells[1]:
			a1 = shells[0]
			a2 = shells[1]
			shells[0] = a2
			shells[1] = a1
			
		if shells[2] > shells[3]:
			a3 = shells[2]
			a4 = shells[3]
			shells[2] = a4
			shells[3] = a3
			
		#Loopen über alle isospins und spins
		if (J_max - J_min) <= 5:
			for k in range(T_min,T_max+1):
				for l in range(J_min,J_max+1):
				
				#Falls nur 6 Einträge da sind, ist nur eine Zeile an TBME da und nichts ist zu beachten
					#if (J_max - J_min) <= 5:
					
					if data[i+k+1][l-J_min] > 0:
						f.write("  " + str(shells[0]) + "  " + str(shells[1]) + "  " + str(shells[2]) + "  " + str(shells[3]) + "    " + str(l) + "  " + str(k) + "    "  + str("%.4f") % (data[i+k+1][l-J_min]) )
						f.write("\n")
					elif data[i+k+1][l-J_min] < 0:
					
						f.write("  " + str(shells[0]) + "  " + str(shells[1]) + "  " + str(shells[2]) + "  " + str(shells[3]) + "    " + str(l) + "  " + str(k) + "   "  + str("%.4f") % (data[i+k+1][l-J_min]) )
						f.write("\n")
					
				#Falls es mehr als 6 Einträge sind, gibt es einen Zeilenumbruch, s.d. aufgepasst werden muss:
				#2*T wird für den Index der Einträge verwendet, sowie erst +1 dann +2 in data[i+k+1][l-J_min]
		elif (J_max - J_min) > 5:
			for k in range(T_min,T_max+1):	
				for l1 in range(J_min,J_min+6):
						
					if data[i+2*k+1][l1-J_min] > 0:
						f.write("  " + str(shells[0]) + "  " + str(shells[1]) + "  " + str(shells[2]) + "  " + str(shells[3]) + "    " + str(l1) + "  " + str(k) + "    "  + str("%.4f") % (data[i+2*k+1][l1-J_min]) )
						f.write("\n")
					elif data[i+2*k+1][l1-J_min] < 0:
						f.write("  " + str(shells[0]) + "  " + str(shells[1]) + "  " + str(shells[2]) + "  " + str(shells[3]) + "    " + str(l1) + "  " + str(k) + "   "  + str("%.4f") % (data[i+2*k+1][l1-J_min]) )
						f.write("\n")
				for l2 in range(J_min+6,J_max+1):
						
						#Falls J > 10 muss J ein Zeichen nach links verschoben werden
					if l2 < 10:
					
						if data[i+2*k+2][l2-(J_min+6)] > 0:
							f.write("  " + str(shells[0]) + "  " + str(shells[1]) + "  " + str(shells[2]) + "  " + str(shells[3]) + "    " + str(l2) + "  " + str(k) + "    "  + str("%.4f") % (data[i+2*k+2][l2-(J_min+6)]) )
							f.write("\n")
						elif data[i+2*k+2][l2-(J_min+6)] < 0:
							f.write("  " + str(shells[0]) + "  " + str(shells[1]) + "  " + str(shells[2]) + "  " + str(shells[3]) + "    " + str(l2) + "  " + str(k) + "   "  + str("%.4f") % (data[i+2*k+2][l2-(J_min+6)]) )
							f.write("\n")
							
							
					elif l2 >= 10:
						if data[i+2*k+2][l2-(J_min+6)] > 0:
							f.write("  " + str(shells[0]) + "  " + str(shells[1]) + "  " + str(shells[2]) + "  " + str(shells[3]) + "   " + str(l2) + "  " + str(k) + "    "  + str("%.4f") % (data[i+2*k+2][l2-(J_min+6)]) )
							f.write("\n")
						elif data[i+2*k+2][l2-(J_min+6)] < 0:
							f.write("  " + str(shells[0]) + "  " + str(shells[1]) + "  " + str(shells[2]) + "  " + str(shells[3]) + "   " + str(l2) + "  " + str(k) + "   "  + str("%.4f") % (data[i+2*k+2][l2-(J_min+6)]) )
							f.write("\n")							
					
f.close()

