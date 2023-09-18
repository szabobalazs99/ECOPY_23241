def contains_values(input_list, element):
    return element in input_list

def number_of_elements_in_list(input_list):
    return(len(input_list))

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
    return input_list[start_index:end_index]

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
