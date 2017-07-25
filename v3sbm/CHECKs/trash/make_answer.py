import numpy as np


#--------------------------------------------------
#Settings
#--------------------------------------------------

interaction = "usdb"
modelspace = "sd"
restriction = "n"
len_model = len(modelspace)
len_int = len(interaction)

Z = [8,10]
A = [18,20,22,24]

J_min = 0.0
J_max = 8.0
del_J = 2.0

parity = 2


#--------------------------------------------------
#Write an*s files
#--------------------------------------------------
for j in range(len(Z)):
	
	for i in range(len(A)):
		N_max = 21
	
		f = open("z%ia%i.ans" % (Z[j],A[i]) ,"w")
		f.write("--------------------------------------------------")
		f.write("\n")
		f.write("lpe,   0             ")
		f.write("\n")
		f.write(modelspace + (N_max-len_model)*" " + "!Hi")
		f.write("\n")
		f.write(restriction + (N_max - 1)*" " + "!Hi")
		f.write("\n")
		f.write(interaction + (N_max-len_int)*" " + "!Hi")
		f.write("\n")
		if Z[j] < 10:
		
			f.write("  " + str(Z[j])  + (N_max - 1 - 2)*" " + "!Hi")
		
		elif Z[j] >= 10:
		
			f.write(" " + str(Z[j]) + (N_max - 1 - 2)*" " + "!Hi")
	
		f.write("\n")
	
		if A[i] < 10:
		
			f.write("  " + str(A[i]) + (N_max - 1 - 2)*" " + "!Hi")
		
		elif A[i] < 100 and A[i] >= 10:
		
			f.write(" " + str(A[i]) + (N_max - 1 - 2)*" " + "!Hi")
		
		elif A[i] >= 100:
		
			f.write(str(A[i]) + (N_max -1 -2)*" " + "!Hi")		
		f.write("\n")
		f.write(" " + str(round(J_min,1)) + ", " + str(round(J_max,1)) + ", " + str(round(del_J,1)) + ",      ")
		f.write("\n")
		f.write("  " + str(parity) + (N_max -1 -2)*" " + "!Hi")
		f.write("\n")
		f.write("--------------------------------------------------")
		f.write("\n")
		f.write("st" + (N_max -2)*" " + "!Hi")
		f.close()
	
