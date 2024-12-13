import pandas as pd
import matplotlib.pyplot as plt

# Load the data
barnes_matches = pd.read_csv('arnes_refereed_matches.csv')
other_matches = pd.read_csv('other_refs.csv')

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

# Check for any NaT values after conversion
print("\nBarnes Matches Dates after Conversion:")
print(barnes_matches['date'])

print("\nOther Matches Dates after Conversion:")
print(other_matches['date'])

# Count total matches before filtering
total_barnes_matches = barnes_matches.shape[0]
total_other_matches = other_matches.shape[0]

print(f"\nTotal Barnes Matches: {total_barnes_matches}")
print(f"Total Other Matches: {total_other_matches}")

# Extract unique dates from barnes_matches, dropping NaT values
barnes_dates = barnes_matches['date'].dropna().unique()

# Remove records from other_matches that match dates in barnes_matches
other_matches_no_barnes = other_matches[~other_matches['date'].isin(barnes_dates)]

# Identify removed records
removed_records = other_matches[other_matches['date'].isin(barnes_dates)]

# Print the removed records
print("\nRemoved Records from Other Matches (matching dates with Barnes matches):")
print(removed_records)

# Analyze winning statistics for matches refereed by Wayne Barnes
barnes_wins = barnes_matches[barnes_matches['nz_points'] > barnes_matches['opponent_points']].shape[0]
barnes_losses = barnes_matches[barnes_matches['nz_points'] < barnes_matches['opponent_points']].shape[0]
barnes_draws = barnes_matches[barnes_matches['nz_points'] == barnes_matches['opponent_points']].shape[0]

# Analyze winning statistics for matches not refereed by Wayne Barnes
other_wins = other_matches_no_barnes[other_matches_no_barnes['nz_points'] > other_matches_no_barnes['opponent_points']].shape[0]
other_losses = other_matches_no_barnes[other_matches_no_barnes['nz_points'] < other_matches_no_barnes['opponent_points']].shape[0]
other_draws = other_matches_no_barnes[other_matches_no_barnes['nz_points'] == other_matches_no_barnes['opponent_points']].shape[0]




# Save the DataFrames to new CSV files
barnes_matches.to_csv('barnes_refereed_matches_cleaned.csv', index=False)
other_matches.to_csv('other_refs_cleaned.csv', index=False)

