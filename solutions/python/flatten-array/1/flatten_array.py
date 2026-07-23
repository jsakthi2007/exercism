def flatten(iterable):
    result = []

    for item in iterable:
        if item is None:
            continue
        elif isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


# Example
print(flatten([1, [2, 6, None], [[None, [4]], 5]]))