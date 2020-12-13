#!/usr/bin/python
from context import flatten_array_recursive


def run_test_flatten_array():
    # defined test input and expected output
    test_array_1 = [[1, 2, [3]], 4]
    test_array_1_result = [1, 2, 3, 4]
    test_array_2 = [[[[1]]]]
    test_array_2_result = [1]
    test_array_3 = [[[[-1]]]]
    test_array_3_result = [-1]
    test_array_4 = [[1, 2, [-3]], -4]
    test_array_4_result = [1, 2, -3, -4]
    test_array_5 = []
    test_array_5_result = []
    test_array_6 = [1, 2, 3, 4]
    test_array_6_result = [1, 2, 3, 4]

    # test flatten_array_recursive correctness
    assert flatten_array_recursive(test_array_1) == test_array_1_result
    assert flatten_array_recursive(test_array_2) == test_array_2_result
    assert flatten_array_recursive(test_array_3) == test_array_3_result
    assert flatten_array_recursive(test_array_4) == test_array_4_result
    assert flatten_array_recursive(test_array_5) == test_array_5_result
    assert flatten_array_recursive(test_array_6) == test_array_6_result
    assert flatten_array_recursive(test_array_1) == test_array_1_result
    print('all tests passed for flatten array')


if __name__ == '__main__':
    run_test_flatten_array()
