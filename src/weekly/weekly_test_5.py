import pandas
import pandas as pd
from typing import List, Dict
import matplotlib
import matplotlib.pyplot as plt



def change_price_to_float(input_df):
    copy_df = input_df.copy()

    copy_df['item_price'] = copy_df['item_price'].str.replace('$', '').astype(float)

    return copy_df


def number_of_observations(input_df):
    return input_df.shape[0]


def items_and_prices(input_df):
    return input_df[['item_name', 'item_price']]


def sorted_by_price(input_df):
    return input_df.sort_values(by='item_price', ascending=False)


def avg_price(input_df):
    return input_df['item_price'].mean()


def unique_items_over_ten_dollars(input_df):
    copy_df = input_df.copy()
    filtered_df = copy_df[copy_df['item_price'] > 10]
    filtered_df2 = filtered_df.drop_duplicates(subset=['item_name', 'choice_description', 'item_price'])
    return filtered_df2.drop(['order_id', 'quantity'], axis='columns')


def items_starting_with_s(input_df):
    copy_df = input_df.copy()
    filtered_df = copy_df[copy_df['item_name'].str.startswith('S')]

    result = filtered_df['item_name'].unique()
    return pd.Series(result, name='item_name')


def first_three_columns(input_df):
    return input_df.iloc[:, :3]


def every_column_except_last_two(input_df):
    return input_df.iloc[:, :-2]


def sliced_view(input_df, columns_to_keep, column_to_filter, rows_to_keep):
    filtered_df = input_df[input_df[column_to_filter].isin(rows_to_keep)]
    return filtered_df[columns_to_keep]


def generate_quartile(input_df):
    copy_df = input_df.copy()
    quartile_labels = ['low-cost', 'medium-cost', 'high-cost', 'premium']
    quartile_bins = [0, 9.99, 19.99, 29.99, float('inf')]
    copy_df['Quartile'] = pd.cut(input_df['item_price'], bins=quartile_bins, labels=quartile_labels).astype('object')
    return copy_df


def average_price_in_quartiles(input_df):
    copy_df = input_df.copy()
    avg_price_in_quartiles = copy_df.groupby('Quartile')['item_price'].mean().reset_index()

    return avg_price_in_quartiles['item_price']


def minmaxmean_price_in_quartile(input_df):
    copy_df = input_df.copy()
    minmax_blocks = copy_df.groupby('Quartile')['item_price'].agg(['min', 'max', 'mean']).reset_index(drop=True)
    return minmax_blocks


def gen_uniform_mean_trajectories(distribution, number_of_trajectories, length_of_trajectory):
    distribution.rand.seed(42)

    trajectories = []

    for _ in range(number_of_trajectories):
        trajectory = []
        cumulative_sum = 0.0

        for _ in range(length_of_trajectory):
            random_number = distribution.gen_rand()
            cumulative_sum += random_number
            trajectory.append(cumulative_sum / (len(trajectory) + 1))

        trajectories.append(trajectory)

    return trajectories


def gen_logistic_mean_trajectories(distribution, number_of_trajectories, length_of_trajectory):
    distribution.rand.seed(42)

    trajectories = []

    for _ in range(number_of_trajectories):
        trajectory = []
        cumulative_sum = 0.0

        for _ in range(length_of_trajectory):
            random_number = distribution.gen_rand()
            cumulative_sum += random_number
            trajectory.append(cumulative_sum / (len(trajectory) + 1))

        trajectories.append(trajectory)

    return trajectories


def gen_laplace_mean_trajectories(distribution, number_of_trajectories, length_of_trajectory):
    distribution.rand.seed(42)

    trajectories = []

    for _ in range(number_of_trajectories):
        trajectory = []
        cumulative_sum = 0.0

        for _ in range(length_of_trajectory):
            random_number = distribution.gen_rand()
            cumulative_sum += random_number
            trajectory.append(cumulative_sum / (len(trajectory) + 1))

        trajectories.append(trajectory)

    return trajectories


def gen_cauchy_mean_trajectories(distribution, number_of_trajectories, length_of_trajectory):
    distribution.rand.seed(42)

    trajectories = []

    for _ in range(number_of_trajectories):
        trajectory = []
        cumulative_sum = 0.0

        for _ in range(length_of_trajectory):
            random_number = distribution.gen_rand()
            cumulative_sum += random_number
            trajectory.append(cumulative_sum / (len(trajectory) + 1))

        trajectories.append(trajectory)

    return trajectories


def gen_chi2_mean_trajectories(distribution, number_of_trajectories, length_of_trajectory):
    distribution.rand.seed(42)

    trajectories = []

    for _ in range(number_of_trajectories):
        trajectory = []
        cumulative_sum = 0.0

        for _ in range(length_of_trajectory):
            random_number = distribution.gen_rand()
            cumulative_sum += random_number
            trajectory.append(cumulative_sum / (len(trajectory) + 1))

        trajectories.append(trajectory)

    return trajectories

