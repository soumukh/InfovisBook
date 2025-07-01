import matplotlib.pyplot as plt

# Step 1: Define the data
teams = ['West Indies', 'India', 'Australia', 'Pakistan', 'Sri Lanka', 'England']
wins = [2, 2, 6, 1, 1, 1]

# Step 2: Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Step 3: Draw the bar chart
bars = ax.bar(teams, wins, color='steelblue')

# Step 4: Set the title and axis labels
ax.set_title('ODI Cricket World Cup Titles by Country', fontsize=16)
ax.set_xlabel('Teams', fontsize=12)
ax.set_ylabel('Number of Titles', fontsize=12)

# Step 5: Add the number of titles as labels on top of each bar
for bar in bars:
    height = bar.get_height()  # Get the height of each bar
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.1,
            f'{int(height)}', ha='center', va='bottom', fontsize=10)

# Step 6: Set team names as x-axis labels (without years to avoid overlap)
ax.set_xticks(range(len(teams)))
ax.set_xticklabels(teams, rotation=0, ha='center', fontsize=10)

# Step 7: Add grid lines for the y-axis
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Step 8: Adjust layout to prevent clipping
plt.tight_layout()

# Step 9: Display the plot
plt.show()

