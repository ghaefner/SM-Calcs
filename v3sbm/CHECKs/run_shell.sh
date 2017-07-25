#!/bin/bash

#Make answer files
python3 ~/Dokumente/v3sbm/CHECKs/make_answer.py

source ~/Dokumente/nushellx/linux/.bash_profile
 
#Run shell
shell z8a18.ans
. z8a18.bat

shell z8a20.ans
. z8a20.bat

shell z8a22.ans
. z8a22.bat

shell z8a24.ans
. z8a24.bat

shell z10a18.ans
. z10a18.bat

shell z10a20.ans
. z8a18.bat

shell z10a22.ans
. z10a22.bat

shell z10a24.ans
. z10a24.bat


#Get only lpt/eps files
mkdir energies/
cp *lpt energies/.
cp *eps energies/.
mkdir temp/
mv *.py temp/.
mv *.sh temp/.
rm *
mv temp/* .
rm -r temp/
