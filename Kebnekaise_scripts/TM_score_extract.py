from __future__ import division
import sys
import linecache
import Bio.PDB
import numpy
import csv


# filename and number of lines requested

TM_name = sys.argv[1]
Pcomb = sys.argv[2]

#c_filename = sys.argv[4]
#out= sys.argv[2]

#pdb_filename = pdb_code + ".pdb" #not the full cage!

# count the total number of lines
tot_lines = len(open(TM_name).readlines())

TM = list(linecache.getline(TM_name,18))

    
#print test
TM_score=""
for i in range(10,17):
    TM_score+= str(TM[i])


#Pcomb
Pcons=""
with open(Pcomb) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    for line in csv_file:
        if "_model1.pdb" in line:
            for i in range(59,64):
                Pcons+= str(line[i])
        else:
            continue
		
print TM_name[-8:], TM_score, Pcons 
