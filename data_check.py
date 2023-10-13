import pandas as pd

# Load the CSV into a DataFrame
commits_df = pd.read_csv('commit_messages_fromated.csv')

# Count unique authors
unique_authors = commits_df['NEAR_DEV'].nunique()
print(f"Number of unique authors: {unique_authors}")

# Convert the 'Time' column to datetime format using mixed format option and extract the date part
commits_df['Date'] = pd.to_datetime(commits_df['TX_TIME'], format='mixed').apply(lambda x: x.date())



# Sort the dataframe by TX_TIME
commits_df_sorted = commits_df.sort_values(by='TX_TIME')




# Group by date and count all developers (non-unique)
active_devs_per_day = commits_df.groupby('Date').size()

# Reset the index to get it into a DataFrame
active_devs_per_day = active_devs_per_day.reset_index()

# Rename columns for clarity
active_devs_per_day.columns = ['Date', 'Unique Active Developers']

active_devs_per_day.to_csv('author_activity_per_day.csv', index=False)



# Sort the dataframe by TX_TIME
commits_df_sorted = commits_df.sort_values(by='TX_TIME')

# Group by date and count unique developers
active_devs_per_day = commits_df.groupby('Date')['NEAR_DEV'].nunique()

# Reset the index to get it into a DataFrame
active_devs_per_day = active_devs_per_day.reset_index()

# Rename columns for clarity
active_devs_per_day.columns = ['Date', 'Unique Active Developers']

active_devs_per_day.to_csv('author_activity_per_day_unique.csv', index=False)



