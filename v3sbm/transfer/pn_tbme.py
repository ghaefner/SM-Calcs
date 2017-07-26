import numpy as np
from antoine_to_nushellx import interaction_new
from antoine_to_nushellx import sps


inter = np.loadtxt("%s_m.int" % interaction_new, skiprows=2)

state = [inter[:,0],inter[:,1],inter[:,2],inter[:,3],inter[:,4],inter[:,5],inter[:,6]]

proton = [1,2]
neutron = [3,4,5,6,7]
N_tbme = len(state[0])

for i in range(len(state[0])):
	#if state[0][i] in proton and state[1][i] in neutron:
	#	state[6][i] = state[6][i] * 0.5
	a = int(state[0][i])
	b = int(state[1][i])
	c = int(state[2][i])
	d = int(state[3][i])
	if (a == b and c == d):
		continue
	elif (a == b or c == d):
		#print("aa|bc - ab | cc :" + str(a) + "  " + str(b) + "  " + str(c) + "  " + str(d) +  "    " + str(state[6][i]))
		state[6][i] = state[6][i] * np.sqrt(2)
	elif (a != b and c != d):
		#print("ab|cd - ab | cd :" + str(a) + "  " + str(b) + "  " + str(c) + "  " + str(d) + "    " + str(state[6][i]))
		state[6][i] = state[6][i] * 2
	

f = open("%s_pn.int" % interaction_new,"w")
f.write("! v3sb90 interaction copied from ANTOINE")
f.write("\n")

#Single-particle states
f.write("+" + str(N_tbme))	
for i in range(len(sps[1])):
	f.write("      " + str("%.5f" % (sps[1][i])))
f.write("\n")

for j in range(len(state[0])):
	if state[4][j] < 10:
		if state[6][j] < 0:
			f.write(" " + str(int(state[0][j])) + "  " + str(int(state[1][j])) + "  " + str(int(state[2][j])) + "  " + str(int(state[3][j])) + "   " + str(int(state[4][j])) + "  " + str(int(state[5][j])) + "    " + str("%.4f") %(state[6][j]))
		else:
			f.write(" " + str(int(state[0][j])) + "  " + str(int(state[1][j])) + "  " + str(int(state[2][j])) + "  " + str(int(state[3][j])) + "   " + str(int(state[4][j])) + "  " + str(int(state[5][j])) + "     " + str("%.4f") % (state[6][j]))
		f.write("\n")
	elif state[4][j] >= 10:
		if state[6][j] < 0:
			f.write(" " + str(int(state[0][j])) + "  " + str(int(state[1][j])) + "  " + str(int(state[2][j])) + "  " + str(int(state[3][j])) + "  " + str(int(state[4][j])) + "  " + str(int(state[5][j])) + "    " + str("%.4f") %(state[6][j]))
		else:
			f.write(" " + str(int(state[0][j])) + "  " + str(int(state[1][j])) + "  " + str(int(state[2][j])) + "  " + str(int(state[3][j])) + "  " + str(int(state[4][j])) + "  " + str(int(state[5][j])) + "     " + str("%.4f") % (state[6][j]))
		f.write("\n")
		
f.close()

#print(f.read())

