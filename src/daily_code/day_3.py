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


def get_values(data, rating_value):
    """
    Reduce array according to the bit criteria for different rating value
    Args:
        data:
        rating_value:

    Returns:

    """
    values = np.array(list(map(lambda x: list(map(int, list(x[:-1]))), data)))
    for num in range(len(values[0])):
        sum_pos = np.sum(values, axis=0)[num]
        if sum_pos >= len(values) / 2:
            # bit 1 is more in position num
            remove_element = rating_value[0]
        else:
            remove_element = rating_value[1]

        values = values[values[:, num] == remove_element]
        if len(values) == 1:
            return values[0].dot(2 ** np.arange(values[0].size)[::-1])


def day_3_b(path):
    """
    Calculate oxygen_generator_rating * CO2_scrubber_rating
    Args:
        path: Data path

    Returns:

    """
    data = read_file(path=path)
    oxygen_generator_rating = get_values(data=data, rating_value=[1, 0])
    CO2_scrubber_rating = get_values(data=data, rating_value=[0, 1])

    return oxygen_generator_rating * CO2_scrubber_rating




