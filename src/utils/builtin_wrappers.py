import collections


def every_nth(input_list, step_size):
    if step_size < 1:
        print('Step size smaller than 1, input list returned')
        return input_list
    return input_list[::step_size]