from src.utils.helper_functions import read_file


def day_2_a(path):
    """
    Calculate height, depth
    Args:
        path: Data path

    Returns:

    """
    data = read_file(path=path)

    depth = 0
    height = 0
    for move in data:
        move_data = move.split()
        func = move_data[0]
        num = int(move_data[1])
        if func == 'forward':
            depth += num
        elif func == 'down':
            height += num
        elif func == 'up':
            height -= num
        else:
            raise Exception(f"wrong input")
    return depth * height


def day_2_b(path):
    """
    Calculate height, depth, aim
    Args:
        path: Data path

    Returns:

    """
    data = read_file(path=path)

    depth = 0
    height = 0
    aim = 0
    for move in data:
        move_data = move.split()
        func = move_data[0]
        num = int(move_data[1])
        if func == 'forward':
            height += num
            depth += (aim * num)
        elif func == 'down':
            aim += num
        elif func == 'up':
            aim -= num
        else:
            raise Exception(f"wrong input")
    return depth * height
