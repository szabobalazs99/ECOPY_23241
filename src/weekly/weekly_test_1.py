def evens_from_list(input_list):
    even_values = []
    for item in input_list:
        if item % 2 == 0:
            even_values.append(item)
    return even_values

def every_element_is_odd(input_list):
    for elem in input_list:
        if elem % 2 == 0:
            return False
    return True

def kth_largest_in_list(input_list, kth_largest):
    input_list.sort()
    return input_list[-kth_largest]


def cumavg_list(input_list):
    if not input_list:
        return []

    cum_avg = [input_list[0]]
    for i in range(1, len(input_list)):
        current_avg = (cum_avg[-1] * i + input_list[i]) / (i + 1)
        cum_avg.append(current_avg)

    return cum_avg

def element_wise_multiplication(input_list1, input_list2):
    import numpy as np
    np_array1 = np.array(input_list1)
    np_array2 = np.array(input_list2)
    multiplication = np_array1 * np_array2
    return list(multiplication)

def merge_lists(*lists):
    merged_list = []
    for l in lists:
        merged_list.extend(l)
    return merged_list

def squared_odds(input_list):
    result = []
    for num in input_list:
        if num % 2 != 0:
            result.append(num ** 2)
    return result

def reverse_sort_by_key(input_dict):
    return dict(sorted(input_dict.items(), reverse=True))


def sort_list_by_divisibility(input_list):
    result_dict = {
        'by_two': [],
        'by_five': [],
        'by_two_and_five': [],
        'by_none': [],
    }

    for num in input_list:
        if num % 2 == 0 and num % 5 == 0:
            result_dict['by_two_and_five'].append(num)
        elif num % 2 == 0:
            result_dict['by_two'].append(num)
        elif num % 5 == 0:
            result_dict['by_five'].append(num)
        else:
            result_dict['by_none'].append(num)

    return result_dict