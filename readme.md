

# SocialDB Smart Contract Metrics (BOS Widgets):

1. git pull the archive from github: https://github.com/NEAR-Analytics/NEAR_SOCIAL_DB_WIDGETS
2. run `extract_commits.py`, to generate a time series of commits per day.
   1. update `repo_path` to where the archive is located
3. then run `data_check.py`, this will create the timeseries for unique and overall dev count overtime.