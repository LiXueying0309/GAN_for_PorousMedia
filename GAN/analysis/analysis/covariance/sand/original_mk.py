import csv
import os
from itertools import islice
import numpy as np
import pandas as pd

def read_csv(csvFile):
    with open(csvFile,'r') as read_file:
        reader = csv.reader(read_file)
        for row in islice(reader, 1, None):
            print(row)
    return row

orig_sand = os.listdir("D:\ProgramGAN\data\sand_results\sand_mk_syn/")
data = []

for filename in orig_sand:
    datafile = read_csv("D:\ProgramGAN\data\sand_results\sand_mk_syn/" + filename)
    data.append(datafile)

print(np.array(data).shape)

V = list(range(119))
SA = list(range(119))
MB = list(range(119))
EN = list(range(119))

for i in range(119):
    V[i] = data[i][0]
    SA[i] = data[i][1]
    MB[i] = data[i][2]
    EN[i] = data[i][3]
    
textfile = pd.DataFrame(data=data)
textfile.to_csv('syn_mk.csv')
