import pandas as pd
import matplotlib.pyplot as plt

# Scales small_df to be normalized in the same time window as large_df
def scale_df(large_df, small_df, value_large_df, value_small_df):
    '''
    Scales small_df to be scaled in the same time window as large_df

    large_df: time series normalized within a larger time window
    small_df: time series normalized within a smaller time window
    value_large_df: value indexer for large_df
    value_small_df: value indexer for small_df
    '''
    df_list = []

    for i in range(len(large_df)):
        scaler = large_df[value_large_df][i]

        if i == len(large_df) - 1:
            mask = (small_df['date'] >= large_df['date'][i]) & (small_df['date'] < '2022-09-01')
        else:
            mask = (small_df['date'] >= large_df['date'][i]) & (small_df['date'] < large_df['date'][i+1])
        
        scaled_df = small_df.loc[mask].copy()
        scaled_df[value_small_df] = scaled_df[value_small_df] * scaler

        df_list.append(scaled_df)

    return pd.concat(df_list)


def scale_and_normalize_df(monthly, weekly, hourly):
    '''
    Scales hourly to the time window 2017 till present, and then normalizes the data

    monthly: monthly time series normalized between 2017 till present
    weekly: weekly time series normalized monthly
    hourly: hourly time series normalized weekly
    '''
    scaled_weekly_df = scale_df(monthly, weekly, 'value_month', 'value_week')
    scaled_hourly_df = scale_df(scaled_weekly_df, hourly, 'value_week', 'value_hour')

    max_value = max(scaled_hourly_df['value_hour'])
    min_value = min(scaled_hourly_df['value_hour'])

    normalized_hourly_df = scaled_hourly_df.copy()

    normalized_hourly_df['value_hour'] = scaled_hourly_df['value_hour'].apply(lambda x: ((x - min_value)/(max_value - min_value)) * 100)

    return normalized_hourly_df



# Reading in data:
monthly_df = pd.read_csv('monthly_data.csv')
weekly_df = pd.read_csv('weekly_data.csv')
hourly_df = pd.read_csv('hourly_data.csv')

# Getting the hourly data, normalized within the time window of 2017 to present, and saving
hourly_df_2017_to_present = scale_and_normalize_df(monthly_df, weekly_df, hourly_df)
hourly_df_2017_to_present.to_csv('output/hourly_df_2017_to_present.csv')

# Produces plot of results
ax=plt.gca()
hourly_df_2017_to_present.plot(kind='line',x='date',y='value_hour',color='blue', ax=ax)
plt.savefig('output/hourly_df_plot.png')