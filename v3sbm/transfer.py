import numpy as np

inter = np.loadtxt("v3sbm2.int")

state = [inter[:,0],inter[:,1],inter[:,2],inter[:,3],inter[:,4],inter[:,5],inter[:,6]]

proton = [1,2]
neutron = [3,4,5,6,7]

for i in range(len(state[0])):
	if state[0][i] in proton:
		if state[1][i] in neutron:
			state[6][i] = state[6][i] * 2
			
			#print state[4][i]

f = open("v3.int","w")

for j in range(len(state[0])):
	if state[6][j] < 0:
		f.write(" " + str(int(state[0][j])) + "  " + str(int(state[1][j])) + "  " + str(int(state[2][j])) + "  " + str(int(state[3][j])) + "   " + str(int(state[4][j])) + "  " + str(int(state[5][j])) + "    " + str((state[6][j])))
	else:
		f.write(" " + str(int(state[0][j])) + "  " + str(int(state[1][j])) + "  " + str(int(state[2][j])) + "  " + str(int(state[3][j])) + "   " + str(int(state[4][j])) + "  " + str(int(state[5][j])) + "     " + str((state[6][j])))
	f.write("\n")
		
f.close()

#print(f.read())
