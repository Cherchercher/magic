# Magic coding challenge

# Scope

Must have:

- Functional scrips
- Test Coverage
- Comments for functions and code code

Nice to have:

- Optimized run time
- Documentation and sample usage for each method

# Assumptions:

For Part II and Part III of temperature analysis, if a tie occurs returns the first record with maximum fluctuations.

For Part III of temperature analysis, both start and end dates are inclusive.

# Considerations

Flatten array is written without any library as a recusive function. We go through each integer in the array eactly once hence the function runs in O(N).

Temperature analysis is written with the Pandas package, a very common tool for data processing and analysis. It provides abilities to read and process csv files in fewer lines of code but might be obscure for some who have not used it before.

# Set up

- FORK this repo
- Download forked repo and run `make init`

# Running the functions
```
from answers import flatten_array_recursive
test_array_1 = [[1, 2, [3]], 4]
flatten_array_recursive(test_array_1)
```

- temperature_analysis

arguments:
python file_to_execute path_to_csv_file start_date_in_float (inclusive) end_date_in_float (inclusive)

Example command line input:
`python answers/temperature_analysis.py ../downloads/data.csv 2000.0 2000.456`

Example command line output:
`lowest temperature in the dataset occurs in station_id 676223, date 2010.5420000000001. maximum temperature fluctuation across all dates occurs in station_id 735181. maximum temperature fluctuation in date range 2000.0 - 2000.456 occurs in station_id 659516.`

# Testing

- save test files in format of test_module_to_test
- add tests to `tests/__main__.py`
- `make test`

# Final Thoughts

If I spend more time on this, I will check for valid data input and brainstorm on more edge test cases.

I will implement temperature data analsysis without pandas to see if there's improvements on runtime and readability.

I will evaluation my solutions against the scale of the problem in production (e.g. how much temperature data are we analyzing? how often is the analysis being run? how big of an array are we flattening?)
