def contains_values(input_list, element):
    return element in input_list

def number_of_elements_in_list(input_list):
    return len(input_list)

def remove_every_element_from_list(input_list):
    input_list.clear()

def reverse_list(input_list):
    return list(reversed(input_list))

def odds_from_list(input_list):
    odd_values = []
    for item in input_list:
        if item % 2 != 0:
            odd_values.append(item)
    return odd_values

def number_of_odds_in_list(input_list):
    count = 0
    for item in input_list:
        if item % 2 != 0:
            count += 1
    return count

def contains_odd(input_list):
    for item in input_list:
        if item % 2 != 0:
            return True
    return False

def second_largest_in_list(input_list):
    input_list.sort()
    return input_list[-2]

def sum_of_elements_in_list(input_list):
    return float(sum(input_list))

def cumsum_list(input_list):
    result = []
    current_sum = 0

    for item in input_list:
        current_sum += item
        result.append(current_sum)

    return result

def element_wise_sum(input_list1, input_list2):
	result = []

	for i in range(len(input_list1)):
		result.append(input_list1[i] + input_list2[i])

	return result

def subset_of_list(input_list, start_index, end_index):
    return input_list[start_index:end_index+1]

def every_nth(input_list, step_size):
    return input_list[::step_size]

def only_unique_in_list(input_list):
    return len(input_list) == len(set(input_list))

def keep_unique(input_list):
    return list(set(input_list))

def swap(input_list, first_index, second_index):
    input_list[first_index], input_list[second_index] = input_list[second_index], input_list[first_index]
    return input_list

def remove_element_by_value(input_list, value_to_remove):
        input_list.remove(value_to_remove)
        return input_list

def remove_element_by_index(input_list, index):
    del input_list[index]
    return input_list

def multiply_every_element(input_list, multiplier):
    return [x * multiplier for x in input_list]

def remove_key(input_dict, key):
    if key in input_dict:
        del input_dict[key]
    return input_dict

def sort_by_key(input_dict):
    return dict(sorted(input_dict.items()))

def sum_in_dict(input_dict):
    return float(sum(input_dict.values()))

def merge_two_dicts(input_dict1, input_dict2):
    merged_dict = input_dict1.copy()
    merged_dict.update(input_dict2)
    return merged_dict

def merge_dicts(*dicts):
    merged_dict = {}
    for d in dicts:
        merged_dict.update(d)
    return merged_dict

def sort_list_by_parity(input_list):
    result = {'even': [], 'odd': []}
    for num in input_list:
        result['even'].append(num) if num % 2 == 0 else result['odd'].append(num)
    return result

def mean_by_key_value(input_dict):
    result_dict = {}
    for key, value_list in input_dict.items():
        mean_value = sum(value_list) / len(value_list)
        result_dict[key] = mean_value
    return result_dict

def count_frequency(input_list):
    frequency = {}
    for item in input_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency