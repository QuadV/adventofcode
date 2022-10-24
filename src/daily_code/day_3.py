from src.utils.helper_functions import read_file


def day_3_a(path):
    """
    Calculate
    Args:
        path: Data path

    Returns:

    """
    data = read_file(path=path)

    for value in data:
        print(value)
        print(bin(int(value, base=2)))
        break

    # binary_mul = lambda a,b : bin(int(a, 2) * int(b, 2))