import pandas as pd
import random
import sys


def lowest_temperature(df):
    """
    Get station_id, date pair with the lowest temperature. When a tie occurs, chose a random pair.
    Args:
    df: dataframe capturing dated temperature in stations
    Returns:
    (station_id, date) tuple
    """
    lowest_temps = df[df.temperature_c == df.temperature_c.min()]
    number_of_min_records = len(lowest_temps)
    record_index = 0
    # default index of element with only one lowest temperature record
    if number_of_min_records > 1:
        # get random record index for two or more lowest temperature records
        record_index = random.randint(0, number_of_min_records-1)
    # get result as (station_id, date) tuple
    return [tuple(x)[1:3] for x in lowest_temps.to_records()][record_index]


def maximum_fluctuation(df):
    """
    Get station_id with the most amount of temperature fluctuation across all dates.
    If there are mul
    Args:
    df: dataframe capturing dated temperature in stations
    Returns:
    station_id
    """
    # group records by station id
    # shift rows down once to calculate difference in current record temperature versus next
    # sum difference for each group to get fluctuation
    return df.groupby('station_id').apply(lambda x:  abs(x['temperature_c'].diff()).sum()).idxmax(axis=1)


def maximum_fluctuation_date_range(df, start_date, end_date):
    """
    Get station_id with the most amount of temperature fluctuation within a date range
    Args:
    df: dataframe capturing dated temperature in stations
    start_date: float representing start date in date range (inclusive)
    end_date: float representing end date in date range (inclusive)
    Returns:
    station_id
    """
    filtered_df = df[(df.date >= start_date) & (df.date <= end_date)]
    return maximum_fluctuation(filtered_df)


if __name__ == '__main__':
    # check for argument completeness and correctness
    if len(sys.argv) != 4:
        print('Missing arguments to run with. Please provide valid file path, start date, and end date')
    try:
        start_date = float(sys.argv[2])
    except:
        print('Start date must be a float. example: 2000.0')
    try:
        end_date = float(sys.argv[3])
    except:
        print('End date must be a positive float. example: 2000.345')
    try:
        temparature_data = pd.read_csv(sys.argv[1])
    except IOError as e:
        print(e)

    # get station and date with lowest temperature
    lowest_temp_station_id, owest_temp_station_date = lowest_temperature(
        temparature_data)
    print('lowest temperature in the dataset occurs in station_id {0}, date {1}.'.format(
        lowest_temp_station_id, owest_temp_station_date))
    # get station and date with maximum fluctuation
    max_fluctuation_id = maximum_fluctuation(temparature_data)
    print('maximum temperature fluctuation across all dates occurs in station_id {0}.'.format(
        max_fluctuation_id))
    # get station and date with maximum fluctuation in date range
    max_fluctuation_range_id = maximum_fluctuation_date_range(
        temparature_data, start_date, end_date)
    print('maximum temperature fluctuation in date range {0} - {1} occurs in station_id {2}.'.format(
        start_date, end_date, max_fluctuation_range_id))
