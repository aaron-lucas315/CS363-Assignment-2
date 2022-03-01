import networkx as nx
##import matplotlib.pyplot as plt

avg_deg = 0
avg_cc = 0
avg_pl = 0

for i in range(30):
    G= nx.erdos_renyi_graph(1000,0.01)
##    nx.draw(G)
##    plt.show()

    lst = nx.degree(G)
    sum = 0
    for degree in lst:
        sum += degree[1]
    avg_deg += sum/len(lst)
    avg_cc += nx.average_clustering(G)
    avg_pl += nx.average_shortest_path_length(G)

print("Avgerage degree: " + str(avg_deg/30))
print("Average clustering coefficient: " + str(avg_cc/30))
print("Average path length: " + str(avg_pl/30))
