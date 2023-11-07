import networkx as nx
import matplotlib.pyplot as plt

# Define weighted network
weighted_edges = [
    ('Miles', 'Gwen', 47),
    ('Miles', 'Miguel', 28),
    ('Miles', 'Jefferson', 27),
    ('Miles', 'The Spot', 23),
    ('Miles', 'Prowler', 20),
    ('Gwen', 'Miguel', 12),
    ('Gwen', 'George', 10),
    ('Gwen', 'The Spot', 7),
    ('George', 'Gwen', 7),
    ('Miles', 'Hobie', 6),
    ('Miles', 'Jessica', 6),
    ('Miles', 'Peter B.', 5),
    ('Miles', 'Lyla', 4),
    ('Miles', 'Max Borne', 3),
    ('Peni', 'Miles', 3),
    ('Miles', 'Spectacular Spider-Man', 3),
    ('George', 'Rio', 2),
    ('Spot', 'Olivia', 1),
    ('Prowler', 'Aaron Davis', 1),
    ('Miles', 'Child', 1),
    ('George', 'Comic Lady', 1),
]

# Create weighted graph
G = nx.Graph()
for u, v, w in weighted_edges:
    G.add_edge(u, v, weight=w)

# Calculate centrality measures
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
clustering_coefficient = nx.clustering(G)

# Draw network graph
pos = nx.spring_layout(G)
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_nodes(G, pos, node_size=300)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=.5, font_size=10)
plt.axis('off')
plt.show()

# Display centrality measures
print("Closeness Centrality:")
for node, centrality in closeness_centrality.items():
    print(f"{node}: {centrality:.10f}")

print("\nBetweenness Centrality:")
for node, centrality in betweenness_centrality.items():
    print(f"{node}: {centrality:.10f}")

print("\nClustering Coefficients:")
for node, coefficient in clustering_coefficient.items():
    print(f"{node}: {coefficient:.10f}")
