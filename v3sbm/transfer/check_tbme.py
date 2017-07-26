import numpy as np

interaction = "v3sb"

m = np.loadtxt("%s_m.int" % interaction, skiprows=2)
pn = np.loadtxt("%s_pn.int" % interaction, skiprows=2)

tbme_m = m[:,6]
tbme_pn = pn[:,6]

#Check length:
if len(tbme_m) != len(tbme_pn):
	print("Error: number of TBME is not equal")
	
#Check difference in TBME
diff = 0.
sum_cross = 0.
sum_m = 0.
sum_pn = 0.

for i in range(len(tbme_m)):
	sum_m += tbme_m[i]
	sum_pn += tbme_pn[i]
	diff += (tbme_m[i] - tbme_pn[i])
	sum_cross += (2*(tbme_m[i]-tbme_pn[i]) - (tbme_m[i] - 2 * tbme_pn[i]))

#Prints and Errors
if diff == 0. :
	print("Error: TBME are equal. Transformation has not been succesful.")	
	exit()

if round(sum_cross,3) != round(sum_m,3):
	print("Error: Cross sums to not match.")
	exit()
	
print("Difference: " + str(diff))
print("Sum TBME non-pn: " + str(sum_m))
print("Sum TBME pn: " + str(sum_pn))
