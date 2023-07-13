import pandas as pd
import numpy as np
import random

# part 2 functions =====================================

adjectives = ['blue', 'large', 'grainy',
              'substantial', 'potent', 'thermonuclear']

nouns = ['food', 'house', 'tree',
         'bicycle', 'toupee', 'phone']


def random_phrase():
    adj = random.choice(adjectives)
    noun = np.random.choice(nouns)
    return adj + " " + noun

# print(random_phrase())
# print(random_phrase())
# print(random_phrase())


def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)
# print(random_float(2, 4))


def random_bowling_score():
    return random.randint(0, 300)
# print(random_bowling_score())


def silly_tuple():
    return (random_phrase(), round(random_float(1, 5)), random_bowling_score())
print(silly_tuple())
print(type(silly_tuple()))
# print(silly_tuple())
# print(silly_tuple())


# def silly_tuple_list(num_tuples):
#     tuple_list = []
#     for item in range(num_tuples):
#         tuple_list.append(silly_tuple())
#     return tuple_list
# print(silly_tuple_list(5))
# # part 3 functions ======================================
# test_df = pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]]))


def null_count(df):
    return df.isnull().sum().sum()


# print(null_count(test_df))

