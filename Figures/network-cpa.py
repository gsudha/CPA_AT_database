#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go
import pandas as pd
import numpy as np
import networkx as nx
import seaborn as sbn
import plotly as plt
from pyvis.network import Network


# In[ ]:





# In[2]:


df=pd.read_csv("CPA_connections",sep="|")


# In[3]:


df


# In[4]:


df["logEvalue"]=np.log(df.evalue)


# In[74]:


df=df.replace("cons1_r1","PSE1_r1")
df=df.replace("cons1_r2","PSE1_r2")
df=df.replace("cons2_r1","PSE2_r1")
df=df.replace("cons2_r2","PSE2_r2")


# In[75]:


sbn.scatterplot(data=df,x="logEvalue",y="probability")


# In[76]:


tempdf=df[df.probability>95]
len(tempdf)


# In[77]:


tempdf=df[df.evalue<0.001]
len(tempdf)


# In[ ]:





# In[78]:


G=nx.from_pandas_edgelist(tempdf,source="repeat1",target="repeat2",edge_attr="score")


# In[79]:


nx.draw_networkx(G)


# In[ ]:





# In[80]:


tempdf[tempdf.evalue>0.001]


# In[81]:


nodes=tempdf.repeat1.unique()
nodes


# In[88]:



colordict={
"abrb_r1":"limegreen",
"abrb_r2":"green",
"antiport_r1":"tomato",
"antiport_r2":"red",
"asp_r1":"limegreen",
"asp_r2":"green",
"cons1_r1":"royalblue",
"cons1_r2":"blue",
"cons2_r1":"royalblue",
"cons2_r2":"blue",
"PSE1_r1":"royalblue",
"PSE1_r2":"blue",
"PSE2_r1":"royalblue",
"PSE2_r2":"blue",
"duf819_r1":"limegreen",
"duf819_r2":"green",
"ex1_r1":"salmon",
"ex1_r2":"red",
"ex2_r1":"salmon",
"ex2_r2":"red",
"glt_r1":"limegreen",
"glt_r2":"green",
"hct_r1":"limegreen",
"hct_r2":"green",
"kdgt_r1":"magenta",
"kdgt_r2":"purple",
"lrga_r1":"royalblue",
"lrgab_r1":"royalblue",
"lrgab_r2":"blue",
"lrgb_r1":"royalblue",
"lrgb_r2":"blue",
"lysa_r1":"royalblue",
"lysab_r1":"royalblue",
"lysab_r2":"blue",
"lysb_r1":"royalblue",
"mt10_r1":"magenta",
"mt10_r2":"purple",
"oad_r1":"limegreen",
"oad_r2":"green",
"sbf10_r1":"magenta",
"sbf10_r2":"purple",
"sbf9_r1":"magenta",
"sbf9_r2":"purple",
"sbflike_r1":"magenta",
"sbflike_r2":"purple",
"sbt1_r1":"magenta",
"sbt1_r2":"purple",
}


# In[94]:


#cutoff=99
#tempdf=df[df.probability>cutoff]
tempdf=df[df.evalue<0.01]
#tempdf=df
G=nx.from_pandas_edgelist(tempdf,source="repeat1",target="repeat2",edge_attr="evalue")


# In[95]:


net=Network(notebook=True,height='400px', width='100%',)
net.from_nx(G)


# In[96]:


for n in net.nodes:
    #print (n)
    n["title"] = n["label"]
    n["color"] = colordict[n["label"]]
    n["font.size"] = 28
    n["borderWidth"]=20


# In[97]:


for e in net.edges:
    #print (e)
    if e["from"]==e["to"]:
        e["value"]=0
        e["hidden"]=True
    else:
        if e["evalue"] < 0.00001:
            e["value"]=3
        elif e["evalue"] < 0.0001: 
            e["value"]=2
        elif e["evalue"] < 0.001: 
            e["value"]=1
        elif e["evalue"] < 0.01: 
            e["value"]=0.1
        elif e["evalue"] < 0.1: 
            e["value"]=0.1            
        else:           
            e["value"]=0.1
        #e["value"]=e["score"]
    if not colordict[e["from"]]==colordict[e["to"]]:
        e["color"]="black"
    #else:
    #    e["color"]="grey"
    #e["physics"]=True


# In[ ]:





# In[98]:


net.show_buttons(filter_=['physics'])
net.show("network.html")


# In[101]:


net.save_graph("network-graph.html")


# In[ ]:


net.set_options('''
var options = 
  "physics": {
    "forceAtlas2Based": {
      "springLength": 100
    },
    "minVelocity": 0.75,
    "solver": "forceAtlas2Based"
  }
''')


# In[ ]:





# In[20]:


import dash
import visdcc


# In[21]:


g = ig.Graph.TupleList(tempdf.itertuples(index=False), directed=True, weights=True, edge_attrs="probability")


# In[ ]:


plot(G)


# In[ ]:


layout=G.layout_kamada_kawai()


# In[ ]:





# In[ ]:





# In[ ]:




