import math as mt
import csv 
import pandas as pd
from matplotlib import pyplot as plt

print("Enter the width of the structure")
B= float(input())

print("Enter the line Preasure Value")
q= float(input())

#create the cvs file
with open('newFile.cvs','w',newline='') as f:
    theWriter = csv.writer(f)

#for cicle to write the rows in the cvs
    for x in range (int(-B),int(B +1)):
       
        for z in range(0,int(3*B)):
            
             if z != 0:
                beta = alpha = mt.atan((x-B/2)/z)
                alpha = mt.atan((x+B/2)/z) - beta
                
                sigmav = q/mt.pi * (alpha + mt.sin(alpha)* mt.cos( alpha + 2*beta ))
                
                if sigmav <0 :
                    sigmav = -1*sigmav
                
                theWriter.writerow([str(x),str(-z),str(sigmav)])

#using pandas to read the cvs file
df = pd.read_csv("newFile.cvs", header=None)


#define columns to plot
xcol = df[0]
zcol = df[1]
sigcol = df[2]

plt.scatter(xcol,zcol,c=sigcol)
plt.show()
