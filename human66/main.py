import igraph
import pylab as pl
import numpy as np
import pandas as pd
from sys import exit
import networkx as nx
from visbrain.objects import (BrainObj, SceneObj, SourceObj, ConnectObj)


# ------------------------------------------------------------------#


def walktrap(adj, steps=5, label="_"):
    conn_indices = np.where(adj)
    weights = adj[conn_indices]
    edges = list(zip(*conn_indices))
    G = igraph.Graph(edges=edges, directed=False)
    comm = G.community_walktrap(weights, steps=steps)
    communities = comm.as_clustering()
    # print comm
    print("%s number of clusters = %d " % (
        label, len(communities)))
    # print "optimal count : ", comm.optimal_count
    return communities
# ------------------------------------------------------------------#


def plotConnections(edges,
                    nodes,
                    title=None,
                    fileName="f",
                    steps=5):

    communities = walktrap(edges, steps=steps)
    edges = np.triu(edges)

    numClusters = len(communities)
    len_clusters = [len(i) for i in communities]
    b_obj = BrainObj('white', translucent=True)

    s_colors = pl.cm.gist_rainbow(np.linspace(0, 1, numClusters))
    s_colors = np.repeat(s_colors, len_clusters, axis=0)
    # print(s_colors)

    # select = edges > 0.01
    # print(type(select), select.shape)
    

    c_obj = ConnectObj("c1",
                       nodes,
                       edges,
                       line_width=2,
                       #    alpha=0.5,
                       select=edges>0.001,
                       color_by="count",
                    #    cmap='Reds',
                    #    dynamic=(0.99, 1.0),
                    #    cmap='viridis', vmin=0.1, vmax=0.3,
                       #    under='gray', over='red'
                       # cmap=lib.discrete_cmap(len(communities)),
                       #    cmap="Reds",
                       )

    s_obj = SourceObj("s1",
                      nodes,
                      data=np.sum(edges, axis=1),
                      color=s_colors,
                      radius_min=20,
                      radius_max=50)

    KW = dict(title_size=20., zoom=1.2)
    sc = SceneObj(bgcolor="white")
    sc.add_to_subplot(c_obj, title=title)
    sc.add_to_subplot(s_obj)
    sc.add_to_subplot(b_obj, use_this_cam=True, rotate="top")
    # sc.preview()
    sc.screenshot(fileName + '.jpg',
                  transparent=False,
                  autocrop=True,
                  dpi=300,
                  print_size=(15, 10),
                  bgcolor="white")
# ------------------------------------------------------------------#


adj = np.loadtxt("dat/C65.dat", dtype=float)
adj /= np.max(adj)
xyz = np.loadtxt("dat/xyz.dat", dtype=float)
plotConnections(adj, xyz, steps=4)
