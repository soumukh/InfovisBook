# Step 1: Import required libraries
import pandas as pd        # For reading CSV files and handling data
import seaborn as sns      # For plotting
import matplotlib.pyplot as plt  # For additional plotting customization

# Step 2: Read the data from CSV file
# Ensure 'odi_wc_winners.csv' is in the same directory as this script
df = pd.read_csv('odi_wc_winners.csv')

# Step 3: Set the plot size for better visibility
plt.figure(figsize=(10, 6))

# Step 4: Create a bar chart using seaborn
# x-axis: Team names, y-axis: Number of championships won
sns.barplot(x='Team', y='Champions', data=df, palette='muted')

# Step 5: Add chart title and axis labels
plt.title('ODI Cricket World Cup Winners')
plt.xlabel('Team')
plt.ylabel('Number of Wins')

# Step 6: Annotate each bar with the number of wins
for index, row in df.iterrows():
    plt.text(index, row['Champions'] + 0.1, row['Champions'],
             ha='center', va='bottom', fontsize=10)

# Step 7: Display the plot
plt.tight_layout()
plt.show()


