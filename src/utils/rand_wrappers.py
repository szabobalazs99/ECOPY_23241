import random

random.random()

random.randint(1, 100)

random.seed(42) # 42: "answer to the ultimate question of Life, the universe, and everything" --> Hitchhiker's Guide to the Galaxy

random.randint(1, 100)

def random_from_list(input_list):
    return random.choice(input_list)

def random_sublist_from_list(input_list, number_of_elements):
    return random.sample(input_list, number_of_elements)

def random_from_string(input_string):
    return random.choice(input_string)

def hundred_small_random():
    return [random.random() for _ in range(100)] # _ means that the variable doesn't matter from the code's POV

def hundred_large_random():
    return [random.randint(10, 1000) for _ in range(100)]

def five_random_number_div_three():
    result = []
    while len(result) < 5:
        num = random.randint(9, 1000)
        if num % 3 == 0:
            result.append(num)
    return result

def random_reorder(input_list):
    new_list = input_list
    random.shuffle(new_list)
    return new_list

def uniform_one_to_five():
    return random.uniform(1, 5)