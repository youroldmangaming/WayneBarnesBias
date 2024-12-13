import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load the cleaned data
barnes_matches = pd.read_csv('barnes_refereed_matches_cleaned.csv')
other_matches = pd.read_csv('other_refs_cleaned.csv')

# Clean the data by stripping whitespace from column names and values
barnes_matches.columns = barnes_matches.columns.str.strip()
other_matches.columns = other_matches.columns.str.strip()

# Strip whitespace from relevant columns
barnes_matches['result'] = barnes_matches['result'].str.strip()
barnes_matches['opponent'] = barnes_matches['opponent'].str.strip()
barnes_matches['referee'] = barnes_matches['referee'].str.strip()

other_matches['result'] = other_matches['result'].str.strip()
other_matches['opponent'] = other_matches['opponent'].str.strip()

# Convert date strings to datetime objects for accurate comparison
barnes_matches['date'] = pd.to_datetime(barnes_matches['date'], format='%a %dth %b %Y %I:%M%p', errors='coerce')
other_matches['date'] = pd.to_datetime(other_matches['date'], format='%a %dth %b %Y %I:%M%p', errors='coerce')

# Analyze winning statistics for matches refereed by Wayne Barnes
barnes_wins = barnes_matches[barnes_matches['nz_points'] > barnes_matches['opponent_points']].shape[0]
barnes_losses = barnes_matches[barnes_matches['nz_points'] < barnes_matches['opponent_points']].shape[0]
barnes_draws = barnes_matches[barnes_matches['nz_points'] == barnes_matches['opponent_points']].shape[0]

# Analyze winning statistics for matches not refereed by Wayne Barnes
other_wins = other_matches[other_matches['nz_points'] > other_matches['opponent_points']].shape[0]
other_losses = other_matches[other_matches['nz_points'] < other_matches['opponent_points']].shape[0]
other_draws = other_matches[other_matches['nz_points'] == other_matches['opponent_points']].shape[0]

# Calculate win/loss ratios
barnes_total = barnes_wins + barnes_losses + barnes_draws
other_total = other_wins + other_losses + other_draws

barnes_win_ratio = barnes_wins / barnes_total if barnes_total > 0 else 0
other_win_ratio = other_wins / other_total if other_total > 0 else 0

print("\nWayne Barnes Refereed Matches:")
print(f"Wins: {barnes_wins}, Losses: {barnes_losses}, Draws: {barnes_draws}")
print(f"Win Ratio: {barnes_win_ratio:.2f}")

print("\nOther Refereed Matches:")
print(f"Wins: {other_wins}, Losses: {other_losses}, Draws: {other_draws}")
print(f"Win Ratio: {other_win_ratio:.2f}")

# Perform statistical analysis (Chi-squared test for independence)
observed = [[barnes_wins, barnes_losses], [other_wins, other_losses]]
chi2, p, _, _ = stats.chi2_contingency(observed)

print(f"\nChi-squared Test Statistic: {chi2:.2f}, p-value: {p:.4f}")

# Visualize the results
labels = ['Wins', 'Losses']
barnes_stats = [barnes_wins, barnes_losses]
other_stats = [other_wins, other_losses]

x = range(len(labels))

plt.bar(x, barnes_stats, width=0.4, label='Barnes', color='blue', align='center')
plt.bar([p + 0.4 for p in x], other_stats, width=0.4, label='Other Referees', color='orange', align='center')

plt.xlabel('Match Outcome')
plt.ylabel('Number of Matches')
plt.title('NZ All Blacks Match Outcomes: Barnes vs Other Referees')
plt.xticks([p + 0.2 for p in x], labels)
plt.legend()
plt.show()

