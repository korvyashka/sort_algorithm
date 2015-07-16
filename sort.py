import sys


def sort_algorithm(data):
    """
    Sorts list of string and integers.
    Output maintain the positions of strings and numbers
     as they appeared in the original list

    :param list data: list to sort

    :rtype: list
    :return: sorted list
    """
    # Negative integers handling
    def _int_mapper(x):
        try:
            int(x)
            return True
        except ValueError:
            return False

    is_int_map = map(_int_mapper, data)
    for i, x in enumerate(is_int_map):
        if x:
            data[i] = int(data[i])

    data.sort()
    result = range(len(data))
    string_indexes = []

    for index, is_int in enumerate(is_int_map):
        if is_int:
            result[index] = str(data.pop(0))
        else:
            string_indexes.append(index)

    for index in string_indexes:
        result[index] = data.pop(0)

    return result


def read_from_std():
    return sys.stdin.readline()


if __name__ == '__main__':
    string = read_from_std()
    data = string.strip().split(' ')
    result = sort_algorithm(data)
    sys.stdout.write(' '.join(result))
