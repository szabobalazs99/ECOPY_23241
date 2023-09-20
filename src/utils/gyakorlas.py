
def element_wise_sum(input_list1, input_list2):
    import numpy as np
    np_array1 = np.array(input_list1)
    np_array2 = np.array(input_list2)
    sum = np_array1 + np_array2
    return list(sum)

my_list_1 = [1, 2, 3, 4, 5, 6, 13, 15.5]
my_list_2 = [4, 7, 3, 9, 5.3, 11, 12, 10]
print(element_wise_sum(my_list_1, my_list_2))

