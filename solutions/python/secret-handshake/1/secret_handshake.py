def commands(binary_str):
    actions = ["wink", "double blink", "close your eyes", "jump"]
    result = [actions[i] for i in range(4) if len(binary_str) > i and binary_str[-(i + 1)] == "1"]
    if len(binary_str) > 4 and binary_str[-5] == "1":
        result.reverse()
    return result