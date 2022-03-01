'''taken from https://networkx.org/documentation/networkx-2.3/auto_examples/drawing/plot_degree_histogram.html'''

import networkx as nx
import matplotlib.pyplot as plt
import collections

G = nx.erdos_renyi_graph(5000,0.01)

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80)

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)

plt.show()
