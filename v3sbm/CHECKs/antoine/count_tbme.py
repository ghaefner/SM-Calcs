#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

#Function to converting strings to numbers: either ints or floats
def num(s):
	try:
		return int(s)
	except ValueError:
		return float(s)


#Read in data: delete first couple of lines as for single-particle energies

with open("usdb_an.int","r") as f:
	all_data = [x.split() for x in f.readlines()]


for i in range(4):		
	del(all_data[i])	
	
for i in range(len(all_data)):
	for j in range(len(all_data[i])):
		all_data[i][j] = num(all_data[i][j])


#TBMEs

tbme = []
tbme_sum = 0.
		
for i in range(len(all_data)):
	if isinstance(all_data[i][0],float):
		
		for j in range(len(all_data[i])):
			if all_data[i][j] != 0. :
				
				tbme.append(all_data[i][j])
				tbme_sum += all_data[i][j]
			
tbme = np.sort(tbme)

#Write file
f = open("usdb_antoine.txt","w")

f.write("TBME from USDB interaction extracted from ANTOINE")
f.write("\n")
f.write("Numbers of TBME: %i" % len(tbme))
f.write("\n")
f.write("Total sum of TBME: %f" % tbme_sum)
f.write("\n")

for i in range(len(tbme)):
	f.write(str(round(tbme[i],4)))
	f.write("\n")
	
f.close()

