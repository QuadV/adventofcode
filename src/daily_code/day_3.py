from src.utils.helper_functions import read_file
import numpy as np


def day_3_a(path):
    """
    Calculate gamma_rate and epsilon_rate
    Args:
        path: Data path

    Returns:

    """
    data = read_file(path=path)
    buckets = np.zeros(len(data[0])-1, int)
    for value in data:
        value_array = np.array(list(map(int, list(value)[:-1])))
        buckets += value_array

    mid_value = len(data) / 2
    gamma_rate = ''
    epsilon_rate = ''
    for value in buckets:
        if value > mid_value:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'
    binary_mul = int(gamma_rate, 2) * int(epsilon_rate, 2)
    return binary_mul


def day_3_b(path):
    """
    Calculate gamma_rate and epsilon_rate
    Args:
        path: Data path

    Returns:

    """
    data = read_file(path=path)

