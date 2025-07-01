# Step 1: Load required libraries
library(ggplot2)

# Step 2: Read the data from the CSV file
# (Make sure 'odi_wc_winners.csv' is in your working directory)
odi_winners <- read.csv("odi_wc_winners.csv", stringsAsFactors = FALSE)

# Step 3: Create the bar chart
ggplot(odi_winners, aes(x = reorder(Team, -Champions), y = Champions, fill = Team)) +
  geom_bar(stat = "identity") +
  labs(
    title = "ODI Cricket World Cup Winners",
    x = "Team",
    y = "Number of Wins"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5, size = 16, face = "bold"),
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "none"
  )
