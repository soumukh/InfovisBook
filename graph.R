# Step 1: Load the igraph package
library(igraph)

# Step 2: Load the built-in Karate Club graph
g <- make_graph("Zachary")  # Zachary's Karate Club graph

# Step 3: Optionally inspect the graph
# print(g)
# summary(g)

# Step 4: Compute a force-directed layout (Fruchterman-Reingold algorithm)
layout <- layout_with_fr(g)

# Step 5: Plot the graph using the layout
plot(
  g,
  layout = layout,         # Use computed layout
  vertex.size = 20,        # Size of the nodes
  vertex.label = V(g)$name,# Node labels
  vertex.color = "skyblue",# Node color
  edge.arrow.size = 0.5,   # Arrow size for edges (not really used here, it's undirected)
  main = "Karate Club Graph (Force-Directed Layout)"
)
