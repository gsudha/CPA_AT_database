import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

df = pd.read_csv("filename.csv", delimiter=',')

# Prepare Data 

# Draw Plot for Each Type
ax = sns.lmplot(x='', y='', data=df)

plt.xticks(fontsize=11); plt.yticks(fontsize=11)
plt.xlabel('name', fontsize=16)
plt.ylabel('name', fontsize=16)
  
plt.figure(facecolor="white")
plt.show()    
