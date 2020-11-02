# coding: utf-8

# In[1]:


import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import re
import pandas as pd

mpl.rcParams.update({'font.size': 14})



# In[2]:


df=pd.read_csv("proteome_lys_grps.csv",sep="|")


# In[3]:


proteomes=df.proteome_id.unique()
#proteomes


# In[4]:


numhits=df.proteome_id.value_counts(dropna=False)
df2=pd.DataFrame.from_dict(numhits)
df2=df2.reset_index()
df2.columns = ['proteome_id', 'numhits']
#df2


# In[5]:


#df


# In[6]:


df=df.merge(df2,on="proteome_id")


# In[8]:

#plt.scatter(df.numhits,df.length)

# In[14]:
sns.set_style("whitegrid")
f, ax = plt.subplots(figsize=(16, 12))
for hue_color,s in zip([True, False], ["proteomes", "proteomes_nocolor"]):
    # fig, ax = plt.subplots(figsize=[9,6])
    # sns.violinplot(data=df, x="numhits", y="length", ax=ax)
    violin_plot = sns.violinplot(data=df, x="numhits", y="length", color='gray', scale="count", ax=ax, inner=None)
    for v in violin_plot.collections:
        # print(v)
        v.set_alpha(0.2)
    if hue_color:
        strip_plot = sns.swarmplot(data=df, x="numhits", y="length", hue="proteome_id", ax=ax)
        ax.legend_.remove()
    else:
        strip_plot = sns.swarmplot(data=df, x="numhits", y="length",ax=ax)
    sns.despine(bottom=False, left=False, ax=ax)
    #sns.set(rc={'figure.figsize':(11.7,8.27)})
    ax.set(xlabel="Number of hits in a proteome",ylabel="Length of protein",ylim=[0,450], yticks=[0,100,200,300,400])
    plt.tight_layout()
    for ext in [".png", ".tiff"]:
        ax.get_figure().savefig(s + ext)
    ax.cla()

