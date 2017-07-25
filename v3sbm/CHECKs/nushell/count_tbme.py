import numpy as np

#READ IN INTERACTION: CHECK FOR COMMENT LINES IF INTERACTION IS CHANGES
w_int = np.loadtxt("usdb.int", skiprows = 7)

tbme = w_int[:,6]

tbme = np.sort(tbme)

tbme_sum = 0.

for i in range(len(tbme)):
	tbme_sum += tbme[i]


f = open("usdb_nushell.txt","w")

#HEADER
f.write("TBME from USDB interaction extracted from NushellX")
f.write("\n")
f.write("Numbers of TBME: %i" % len(tbme))
f.write("\n")
f.write("Total sum of TBME: %f" % tbme_sum)
f.write("\n")

for i in range(len(tbme)):
	f.write(str(round(tbme[i],4)))
	f.write("\n")
	
f.close()

print(tbme)
