import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt 
from networkx.drawing.nx_agraph import graphviz_layout


def plot_graph(G, G2=None, nodelist=None, pos=None, figsize=[40, 20], edge_color='b', edge_color2='r', node_size=2500, node_color='y', font_size=12, label=True, width= None):
    if pos is None:
        if G2 is not None:
            g = nx.compose(G, G2)
            pos = graphviz_layout(g, prog='dot')
        else:
            pos = graphviz_layout(G, prog='dot')
    if nodelist is None:
        nodelist = list(G.nodes)
    if width == 'r':
        width = [np.abs(G[u][v]['weight']) for u, v in G.edges * 2]

    plt.figure(figsize=figsize)
    nx.draw_networkx(G,
                     pos=pos,
                     nodelist = nodelist,
                     width = width, 
                     edge_color=edge_color, 
                     node_size=node_size, 
                     node_color=node_color,
                     font_size=font_size)
    if label is True:
        nx.draw_networkx_edge_labels(G,
                                     pos=pos, 
                                     edge_labels={i: f"{G.edges[i]['weight']:.2f}" for i in G.edges},
                                     font_size=font_size)

    if G2 is not None:
        nx.draw_networkx_edges(G2,
                               pos=pos,
                               nodelist=nodelist,
 #                              width=[np.abs(G2[u][v]['weight']) for u, v in G2.edges],
                               node_size=node_size,
                               edge_color=edge_color2)
        if label is True:
            nx.draw_networkx_edge_labels(G2,
                                         pos=pos, 
                                         edge_labels={i: f"{G2.edges[i]['weight']:.2f}" for i in G2.edges},
                                         font_size=font_size)

                
    

    
  


 
