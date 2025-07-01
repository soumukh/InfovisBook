# Step 1: Define the data inline using vectors
teams <- c("West Indies", "India", "Australia", "Pakistan", "Sri Lanka", "England")
champions <- c(2, 2, 6, 1, 1, 1)

# Step 2: Create a named vector for bar heights
wins <- setNames(champions, teams)

# Step 3: Set up plot window (optional in RStudio)
# windows(width = 8, height = 6)  # Uncomment this on Windows

# Step 4: Draw the barplot
barplot(
  wins,                        # Bar heights
  main = "ODI Cricket World Cup Winners",  # Chart title
  xlab = "Team",               # X-axis label
  ylab = "Number of Wins",     # Y-axis label
  col = "skyblue",             # Bar color
  border = "black",            # Bar border color
  ylim = c(0, max(wins) + 1),  # Leave space above bars
  las = 2                      # Make team labels vertical for clarity
)

# Step 5: Optionally, label bars with win counts
text(
  x = seq_along(wins),         # X positions
  y = wins + 0.2,              # Y positions (just above bars)
  labels = wins,               # Text labels (number of wins)
  cex = 0.9, col = "black"
)
