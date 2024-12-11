import pandas as pd
import matplotlib.pyplot as plt

# Load the data
barnes_matches = pd.read_csv('arnes_refereed_matches.csv')
other_matches = pd.read_csv('other_refees.csv')

# Analyze winning statistics for matches refereed by Wayne Barnes
barnes_wins = barnes_matches[barnes_matches['result'] == 'win'].shape[0]
barnes_losses = barnes_matches[barnes_matches['result'] == 'loss'].shape[0]
barnes_draws = barnes_matches[barnes_matches['result'] == 'draw'].shape[0]

# Analyze winning statistics for matches not refereed by Wayne Barnes
other_wins = other_matches[other_matches['result'] == 'win'].shape[0]
other_losses = other_matches[other_matches['result'] == 'loss'].shape[0]
other_draws = other_matches[other_matches['result'] == 'draw'].shape[0]

# Print results
print("Wayne Barnes Refereed Matches:")
print(f"Wins: {barnes_wins}, Losses: {barnes_losses}, Draws: {barnes_draws}")

print("\nOther Refereed Matches:")
print(f"Wins: {other_wins}, Losses: {other_losses}, Draws: {other_draws}")

# Visualize the results
labels = ['Wins', 'Losses', 'Draws']
barnes_stats = [barnes_wins, barnes_losses, barnes_draws]
other_stats = [other_wins, other_losses, other_draws]

x = range(len(labels))

plt.bar(x, barnes_stats, width=0.4, label='Barnes', color='blue', align='center')
plt.bar([p + 0.4 for p in x], other_stats, width=0.4, label='Other Referees', color='orange', align='center')

plt.xlabel('Match Outcome')
plt.ylabel('Number of Matches')
plt.title('NZ All Blacks Match Outcomes: Barnes vs Other Referees')
plt.xticks([p + 0.2 for p in x], labels)
plt.legend()
plt.show()
