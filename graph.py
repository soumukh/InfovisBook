import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Load the Zachary's Karate Club graph
G = nx.karate_club_graph()

# Step 2: Compute the force-directed layout (spring layout)
pos = nx.spring_layout(G, seed=42)  # seed for reproducibility

# Step 3: Set up the plot
plt.figure(figsize=(10, 8))
plt.title("Zachary's Karate Club Graph (Force-Directed Layout)")

# Step 4: Draw nodes
# We color the nodes by a node attribute -  "club" affiliation 
club_colors = {
    'Mr. Hi': 'skyblue',
    'Officer': 'lightgreen'
}
node_colors = [club_colors[G.nodes[n]['club']] for n in G.nodes]

nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)

# Step 5: Draw edges
nx.draw_networkx_edges(G, pos, alpha=0.6)

# Step 6: Draw node labels
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

# Step 7: Remove axes
plt.axis('off')

# Step 8: Show the plot
plt.show()
