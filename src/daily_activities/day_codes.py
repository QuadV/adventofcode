from src.utils.helper_functions import read_file


def day_1_a(path):
    """
    Consecutive increase in depth
    Args:
        path: Data path

    Returns:

    """
    data = read_file(path=path)

    count_increase = 0
    for i, depth in enumerate(data[1:], start=1):
        if int(depth) > int(data[i-1]):
            count_increase += 1
    return count_increase


def day_1_b(path):
    """
    Window of size 3 increase in depth
    Args:
        path: Data path

    Returns:

    """
    data = read_file(path=path)

    count_increase = 0
    previous_depth = int(data[0]) + int(data[1]) + int(data[2])
    for i in range(1, len(data)-2):
        depth = int(data[i]) + int(data[i+1]) + int(data[i+2])
        if depth > previous_depth:
            count_increase += 1
        previous_depth = depth
    return count_increase