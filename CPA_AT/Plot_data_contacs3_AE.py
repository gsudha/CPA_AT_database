import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sys
align = sys.argv[1] 

df = pd.read_csv(align, sep='\t', header = 0,index_col=0)

print (df)
#sns.axes_style("darkgrid")
f, ax = plt.subplots()

#ax = sns.heatmap(df, cmap='gist_gray',vmin=1, vmax = 10)
ax = sns.heatmap(df, cmap='gist_gray',vmin=8, vmax = 10,cbar=False)

Hhelices=[[5,17],[30,46],[63,86],[118,146],[174,195]]
Hreentrant=[[92,115],[149,168]]
#ax.hlines([26,47,75,239,266,306], *ax.get_xlim(), color='blue',alpha=0#.1)
Vhelices=[[28,43],[51,69],[82,96],[101,130],[134,166],[205,236],[265,289],[300,314],[319,347],[362,383],[417,441]]
Vreentrant=[[170,198],[388,413]]
#ax.vlines([33,64,83,119,239,275,302,341,433], *ax.get_ylim(), color='blue',alpha=0.1)# 1=16 in x ax
#ax.vlines([154,187,372,399], *ax.get_ylim(), color='red',alpha=0.1)# 1=16 in x ax

loop=0
for start,stop in Hhelices:
    start+=loop
    stop+=-loop
    for j in range(start,stop):
        ax.hlines([j], *ax.get_xlim(), color='blue',alpha=0.1)

for start,stop in Hreentrant:
    start+=loop
    stop+=-loop
    for j in range(start,stop):
        ax.hlines([j], *ax.get_xlim(), color='red',alpha=0.1)

for start,stop in Vhelices:
    start+=loop
    stop+=-loop
    for j in range(start,stop):
        ax.vlines([j], *ax.get_xlim(), color='blue',alpha=0.1)

for start,stop in Vreentrant:
    start+=loop
    stop+=-loop
    for j in range(start,stop):
        ax.vlines([j], *ax.get_xlim(), color='red',alpha=0.1)


positions_X = (1,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440)
labels_X = ("1","10","20","30","40","50","60","70","80","90","100","110","120","130","140","150","160","170","180","190","200","210","220","230","240","250","260","270","280","290","300","310","320","330","340","350","360","370","380","390","400","410","420","430","440")
plt.xticks(positions_X, labels_X)

positions_Y = (1,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200)
labels_Y = ("1","10","20","30","40","50","60","70","80","90","100","110","120","130","140","150","160","170","180","190","200")
plt.yticks(positions_Y, labels_Y)

#1=16 in x ax
plt.savefig("Cons2_5a1s_structure_ali", dpi=600)
plt.show()    
