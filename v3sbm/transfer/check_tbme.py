import numpy as np

interaction = "v3sb90"

m = np.loadtxt("%s_m.int" % interaction, skiprows=2)
pn = np.loadtxt("%s_pn.int" % interaction, skiprows=2)

tbme_m = m[:,6]
tbme_pn = pn[:,6]

#Check length:
if len(tbme_m) != len(tbme_pn):
	print("Error: number of TBME is not equal")
	
#Check difference in TBME
diff = 0.
for i in range(len(tbme_m)):
	diff += (tbme_m[i] - tbme_pn[i])
	
print(diff)
