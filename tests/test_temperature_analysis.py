#!/usr/bin/python
import pandas as pd
from context import lowest_temperature, maximum_fluctuation, maximum_fluctuation_date_range


def run_test_temparature_analysis():
    # define test temperature data
    test_temparature_data_1 = {
        'station_id': [68, 68, 68, 69, 69, 69, 70, 70, 70],
        'date': [2000.001, 2000.456, 2000.457, 2000.002, 2000.456, 2000.459, 2000.456, 2000.457, 2002.456],
        'temperature_c': [10.5, 5.4, 5.6, 5.4, 6.9, 10.4, 21.8, 11.5, 19.5]}
    test_temparature_1 = pd.DataFrame(test_temparature_data_1, columns=[
                                      'station_id', 'date', 'temperature_c'])

    test_temparature_data_2 = {
        'station_id': [1, 1, 1],
        'date': [2000.001, 2000.123, 2000.456],
        'temperature_c': [5, 0, 5]}
    test_temparature_2 = pd.DataFrame(test_temparature_data_2, columns=[
                                      'station_id', 'date', 'temperature_c'])

    test_temparature_data_3 = {
        'station_id': [1, 2, 3],
        'date': [2000.001, 2000.123, 2000.456],
        'temperature_c': [5, 0, 5]}
    test_temparature_3 = pd.DataFrame(test_temparature_data_3, columns=[
                                      'station_id', 'date', 'temperature_c'])

    test_temparature_data_4 = {
        'station_id': [1, 2, 3, 2],
        'date': [2000.001, 2000.123, 2000.456, 2000.457],
        'temperature_c': [0, -5, 8, 5]}
    test_temparature_4 = pd.DataFrame(test_temparature_data_4, columns=[
                                      'station_id', 'date', 'temperature_c'])

    # test lowest_temperature
    assert list(lowest_temperature(test_temparature_1)) in [
        [68, 2000.456], [69, 2000.002]]
    assert lowest_temperature(test_temparature_2) == (1, 2000.123)
    assert lowest_temperature(test_temparature_3) == (2, 2000.123)

    # test maximum_fluctuation
    assert maximum_fluctuation(test_temparature_1) == 70
    assert maximum_fluctuation(test_temparature_2) == 1
    assert maximum_fluctuation(test_temparature_3) == 1

    # test maximum_fluctuation_date_range
    assert maximum_fluctuation_date_range(
        test_temparature_1, 2000.001, 2000.456) == 68
    assert maximum_fluctuation_date_range(
        test_temparature_2, 2000.001, 2000.456) == 1
    assert maximum_fluctuation_date_range(
        test_temparature_2, 2000.001, 2000.123) == 1
    assert maximum_fluctuation_date_range(
        test_temparature_3, 2000.001, 2000.123) == 1
    # print(maximum_fluctuation_date_range(
    #     test_temparature_4, 2000.001, 2000.456))
    assert maximum_fluctuation_date_range(
        test_temparature_4, 2000.001, 2000.456) == 1
    assert maximum_fluctuation_date_range(
        test_temparature_4, 2000.001, 2000.457) == 2
    print('all tests passed for temperature analysis')


if __name__ == '__main__':
    run_test_temparature_analysis()
