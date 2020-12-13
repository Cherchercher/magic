def flatten_array_recursive(a):
    """
    recursively flattened nested array of integers
    Args:
    a: array to flatten which each element is either an integer or a (nested) list of integers
    Returns:
    flattened array
    """
    result = []
    for i in a:
        if type(i) == list:
            result += flatten_array_recursive(i)
        else:
            result.append(i)
    return result
