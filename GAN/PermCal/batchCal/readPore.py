# -*- coding: utf-8 -*-
"""
readPore

Created on Sat Jul 24 17:25:43 2021

@author: Xueying
"""

import numpy as np
import h5py
import os
import tifffile
import matplotlib.pyplot as plt
from skimage import img_as_uint

path = "./soil_tif/synthetic/"
files = os.listdir(path)
for filename in files:
    im_in = tifffile.imread(path+filename)
    locl = ''
    for i in range(64):
        for j in range(64):
            for k in range(64):
                if im_in[i][j][k] == 0:
                    locl = "    locationInMesh (" + str(i) + " " + str(j) + " " + str(k) + ");"
                break
   
    line_to_replace = 25 #需要修改的行号，3表示第4行
    my_file = './soil_syn/'+filename[0:8]+'/a/system/snappyHexMeshDict'
    with open(my_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) > int(line_to_replace):
            lines[line_to_replace] = '    '+filename[0:8]+'.stl'+'\n' #new为新参数，记得加换行符\n
            with open(my_file, 'w',encoding='utf-8') as file:
                file.writelines( lines )

    line_to_replace = 70 #需要修改的行号，3表示第4行
    my_file = './soil_syn/'+filename[0:8]+'/a/system/snappyHexMeshDict'
    with open(my_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) > int(line_to_replace):
            lines[line_to_replace] = locl+'\n' #new为新参数，记得加换行符\n
            with open(my_file, 'w',encoding='utf-8') as file:
                file.writelines( lines )  
    
