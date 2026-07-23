def append(list1, list2):
    result = []
    for item in list1:
        result.append(item)
    for item in list2:
        result.append(item)
    return result


def concat(lists):
    result = []
    for lst in lists:
        for item in lst:
            result.append(item)
    return result


def filter(function, values):
    result = []
    for item in values:
        if function(item):
            result.append(item)
    return result


def length(values):
    count = 0
    for _ in values:
        count += 1
    return count


def map(function, values):
    result = []
    for item in values:
        result.append(function(item))
    return result


def foldl(function, values, initial):
    result = initial
    for item in values:
        result = function(result, item)
    return result


def foldr(function, values, initial):
    result = initial
    for i in range(length(values) - 1, -1, -1):
        result = function(result, values[i])
    return result


def reverse(values):
    result = []
    for i in range(length(values) - 1, -1, -1):
        result.append(values[i])
    return result