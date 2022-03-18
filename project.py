import csv
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
sheet="Sheet1"
loc="final.xlsx"


filePtr = pd.read_excel(loc,sheet)
Source_list = filePtr["Unnamed: 6"].tolist()
Destination_list = filePtr["Unnamed: 8"].tolist()
Battery_list = filePtr["Unnamed: 14"].tolist()
print(Source_list)
print(Destination_list)
print(Battery_list)
digraph= nx.DiGraph()
i = 1
while(i<17):
    digraph.add_node(i)
    i = i+1
for i in range(2,1407):
    #print(len(Battery_list))
    digraph.add_edge(Source_list[i],Destination_list[i], weight=float(Battery_list[i]))

graph1 = plt.subplot()
nx.draw(digraph,with_labels = True)
pos = nx.random_layout(digraph, seed=2)
#nx.draw(digraph,pos)
labels = nx.get_edge_attributes(digraph,'weight')
nx.draw_networkx_edge_labels(digraph,pos,edge_labels=labels)
plt.show()