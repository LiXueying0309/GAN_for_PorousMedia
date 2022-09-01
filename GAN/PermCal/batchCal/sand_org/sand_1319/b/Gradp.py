import numpy as np
import requests
#from lxml import etree

def average(list):
    average = sum(list)/len(list)
    return average

def readGradP(filepath):
    lnum = 0
    GradPdata = []
    with open(filepath, 'r') as fd:
        for line in fd:
            lnum += 1;
            if (lnum >= 23) & (lnum <= 42075):
                temp=line.strip('()\n')
                GradPdata.append(temp)
    return GradPdata

U=list(range(1))
time=list(range(1))
for i in range(1):
    time[i] = i+6
    U[i] = readGradP(str(i+6)+"/GradP")
m = list(range(1))
#print(U[3])
for i in range(1):
    for j in range (3):
        m[i] = list(str(U[i]).split( ))
print(np.array(m).shape)
m = np.array(m).reshape(1,3,42053)
Uxav = list(range(1))
Uyav = list(range(1))
Uzav = list(range(1))
Uav = list(range(1))
for i in range(1):
    Ux = list(range(42053))
    Uy = list(range(42053))
    Uz = list(range(42053))
    for j in range(42053):
        Ux[j] = float(m[i][0][j].strip("[',"))
        Uy[j] = float(m[i][1][j].strip("',"))
        Uz[j] = float(m[i][2][j].strip("',]"))
    Uxav[i] = abs(average(Ux))
    Uyav[i] = abs(average(Uy))
    Uzav[i] = abs(average(Uz))
    Uav[i] = np.sqrt(np.square(Uxav[i])+np.square(Uyav[i])+np.square(Uzav[i]))

'''
fig, ax = plt.subplots(2, 2, figsize=(24, 24))
min_x1, max_x1 = 0, 510
min_y1, max_y1 = 0, 2
min_x2, max_x2 = 0, 810
min_y2, max_y2 = 0.9, 1

plt.subplot(221)
ax = plt.gca()
plt.ticklabel_format(style='sci', axis='y')
plt.plot(time_soilorg, Uxav_soilorg, linewidth=4, linestyle='-', color="red", label=r"$Sample \ Data \ (x-axis)$")
plt.plot(time_soilsyn, Uxav_soilsyn, linewidth=4, linestyle='-', color="black", label=r"$Synthetic \ Data \ (x-axis)$")
plt.xlabel("time (s)", fontsize=32, fontproperties='Times New Roman')
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
#plt.xlim(min_x1, max_x1)
#plt.ylim(min_y1, max_y1)
ax.yaxis.major.formatter.set_powerlimits((0,0))
plt.ylabel("velocity (m/s)", fontsize=36, fontproperties='Times New Roman') 
plt.title("Ux", fontsize=40, fontproperties='Times New Roman')    
plt.legend(fontsize=24, loc=2)

plt.subplot(222)
ax = plt.gca()
plt.ticklabel_format(style='sci', axis='y')
plt.plot(time_soilorg, Uyav_soilorg, linewidth=4, linestyle='-', color="red", label=r"$Sample \ Data \ (y-axis)$")
plt.plot(time_soilsyn, Uyav_soilsyn, linewidth=4, linestyle='-', color="black", label=r"$Synthetic \ Data \ (y-axis)$")
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
#plt.xlim(min_x1, max_x1)
plt.ylim(0, 0.05)
ax.yaxis.major.formatter.set_powerlimits((0,0))
plt.ylabel("velocity (m/s)", fontsize=36, fontproperties='Times New Roman') 
plt.title("Uy", fontsize=40, fontproperties='Times New Roman')    
plt.legend(fontsize=24, loc=2)

plt.subplot(223)
ax = plt.gca()
plt.ticklabel_format(style='sci', axis='y')
plt.plot(time_soilorg, Uzav_soilorg, linewidth=4, linestyle='-', color="red", label=r"$Sample \ Data \ (z-axis)$")
plt.plot(time_soilsyn, Uzav_soilsyn, linewidth=4, linestyle='-', color="black", label=r"$Synthetic \ Data \ (z-axis)$")
plt.xlabel("time (s)", fontsize=32, fontproperties='Times New Roman')
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
#plt.xlim(min_x1, max_x1)
plt.ylim(0, 0.03)
ax.yaxis.major.formatter.set_powerlimits((0,0))
plt.ylabel("velocity (m/s)", fontsize=36, fontproperties='Times New Roman') 
plt.title("Uz", fontsize=40, fontproperties='Times New Roman')    
plt.legend(fontsize=24, loc=2)

plt.subplot(224)
ax = plt.gca()
plt.ticklabel_format(style='sci', axis='y')
plt.plot(time_soilorg, Uav_soilorg, linewidth=4, color="red", label=r"$Sample \ Data$")
plt.plot(time_soilsyn, Uav_soilsyn, linewidth=4, color="black", label=r"$Synthetic \ Data$")
plt.xlabel("time (s)", fontsize=32, fontproperties='Times New Roman')
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
#plt.xlim(min_x2, max_x2)
#plt.ylim(min_y2, max_y2)
ax.yaxis.major.formatter.set_powerlimits((0,0))
plt.ylabel("velocity (m/s)", fontsize=36, fontproperties='Times New Roman')
plt.title("U", fontsize=40, fontproperties='Times New Roman')      
plt.legend(fontsize=24, loc=2)

fig.savefig("G:/research/毕业论文/论文/Usoil-time.png", dpi=300)

fig, ax = plt.subplots(1, 1, figsize=(12, 12))
ax = plt.gca()
plt.plot(time_soilorg, Uxav_soilorg, linewidth=4, linestyle='-', color="red", label=r"$Sample \ Data \ (x-axis)$")
plt.plot(time_soilsyn, Uxav_soilsyn, linewidth=4, linestyle='-', color="black", label=r"$Synthetic \ Data \ (x-axis)$")
plt.ticklabel_format(style='sci', axis='y')
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
plt.xlim(0, 400)
plt.ylim(0, 0.05)
ax.yaxis.major.formatter.set_powerlimits((0,0))
fig.savefig("G:/research/毕业论文/论文/Ux_soil-time.png", dpi=300)

fig, ax = plt.subplots(1, 1, figsize=(12, 12))
ax = plt.gca()
plt.plot(time_soilorg, Uyav_soilorg, linewidth=4, linestyle='-', color="red", label=r"$Sample \ Data \ (y-axis)$")
plt.plot(time_soilsyn, Uyav_soilsyn, linewidth=4, linestyle='-', color="black", label=r"$Synthetic \ Data \ (y-axis)$")
plt.ticklabel_format(style='sci', axis='y')
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
plt.xlim(0, 400)
plt.ylim(0, 0.5)
ax.yaxis.major.formatter.set_powerlimits((0,0))
fig.savefig("G:/research/毕业论文/论文/Uy_soil-time.png", dpi=300)

fig, ax = plt.subplots(1, 1, figsize=(12, 12))
ax = plt.gca()
plt.plot(time_soilorg, Uzav_soilorg, linewidth=4, linestyle='-', color="red", label=r"$Sample \ Data \ (z-axis)$")
plt.plot(time_soilsyn, Uzav_soilsyn, linewidth=4, linestyle='-', color="black", label=r"$Synthetic \ Data \ (z-axis)$")
plt.ticklabel_format(style='sci', axis='y')
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
plt.xlim(0, 400)
plt.ylim(0, 0.2)
ax.yaxis.major.formatter.set_powerlimits((0,0))
fig.savefig("G:/research/毕业论文/论文/Uz_soil-time.png", dpi=300)

fig, ax = plt.subplots(1, 1, figsize=(12, 12))
ax = plt.gca()
plt.plot(time_soilorg, Uav_soilorg, linewidth=4, color="red", label=r"$Sample \ Data$")
plt.plot(time_soilsyn, Uav_soilsyn, linewidth=4, color="black", label=r"$Synthetic \ Data$")
plt.ticklabel_format(style='sci', axis='y')
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
plt.xlim(0, 400)
plt.ylim(0, 0.5)
ax.yaxis.major.formatter.set_powerlimits((0,0))
fig.savefig("G:/research/毕业论文/论文/U_soil-time.png", dpi=300)
'''
np.savetxt('GradP_sandorg1201.txt', np.c_[time, Uav], delimiter='\t')
