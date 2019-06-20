import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from openpyxl import load_workbook


wb=load_workbook('rawdata.xlsx')
sheet_ranges=wb['rawdata']
ws2=wb["output"]
soa=([])
for i in range (6,10):
    a=round(sheet_ranges["P"+str(i)].value,3)
    b=round(sheet_ranges["P"+str(i+1)].value,3)
    c=round(sheet_ranges["Q"+str(i)].value,3)
    d=round(sheet_ranges["Q"+str(i+1)].value,3)
    lat=float(b-a)
    lon=float(c-d)
    time=float(ws2["D"+str(i-4)].value)
    soa.append([a, c, 0, lat, lon,time])

    
print(soa)
X, Y, Z, U, V, W = zip(*soa)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W)
   


ax.set_xlim([44, 46])
ax.set_ylim([-92.26, -94])
ax.set_zlim([0, 10])
plt.show()