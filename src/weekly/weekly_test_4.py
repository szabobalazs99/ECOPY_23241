import pandas
import pandas as pd
from typing import List, Dict
import matplotlib
import matplotlib.pyplot as plt


euro12 = pd.read_csv("../../data/Euro_2012_stats_TEAM.csv")


def number_of_participants(input_df):
    return input_df['Team'].nunique()


def goals(input_df):
    return input_df[['Team', 'Goals']]


def sorted_by_goal(input_df):
    return input_df.sort_values(by='Goals', ascending=False)


def avg_goal(input_df):
    return input_df['Goals'].mean()


def countries_over_five(input_df):
    return input_df[input_df['Goals'] >= 6][['Team']]


def countries_starting_with_g(input_df):
    return input_df[input_df['Team'].str.startswith('G')]['Team']


def first_seven_columns(input_df):
    return input_df.iloc[:, :7]


def every_column_except_last_three(input_df):
    return input_df.iloc[:, :-3]


def sliced_view(input_df, columns_to_keep, column_to_filter, rows_to_keep):
    filtered_df = input_df[columns_to_keep]
    filtered_df = filtered_df[filtered_df[column_to_filter].isin(rows_to_keep)]

    return filtered_df


def generate_quarters(input_df):
    copy_df = input_df.copy()
    copy_df['Quartile'] = pd.cut(copy_df['Goals'], bins=[-1, 2, 4, 5, 12], labels=[4, 3, 2, 1]).astype('int64')
    return copy_df


def average_yellow_in_quartiles(input_df):
    copy_df = input_df.copy()
    avg_yellow_in_quartiles = copy_df.groupby('Quartile')['Passes'].mean().reset_index()
    avg_yellow_in_quartiles.drop('Quartile', axis='columns')

    return avg_yellow_in_quartiles['Passes']


def minmax_block_in_quartile(input_df):
    copy_df = input_df.copy()
    return copy_df.groupby('Quartile')['Blocks'].agg(['min', 'max']).reset_index(drop=True)


def scatter_goals_shots(input_df):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(input_df['Goals'], input_df['Shots on target'])

    ax.set_title('Goals and Shot on target')
    ax.set_xlabel('Goals')
    ax.set_ylabel('Shots on target')

    return fig


def scatter_goals_shots_by_quartile(input_df):
    colors = ['red', 'green', 'blue', 'purple']

    unique_quartiles = sorted(input_df['Quartile'].unique())

    fig, ax = plt.subplots(figsize=(10, 6))
    for quartile, color in zip(unique_quartiles, colors):
        quartile_data = input_df[input_df['Quartile'] == quartile]
        ax.scatter(quartile_data['Goals'], quartile_data['Shots on target'], label=f'Quartile {quartile}', c=color)

    ax.set_title('Goals and Shot on target')
    ax.set_xlabel('Goals')
    ax.set_ylabel('Shots on target')

    ax.legend(title='Quartiles')

    return fig


def gen_pareto_mean_trajectories(pareto_distribution, number_of_trajectories, length_of_trajectory):
    pareto_distribution.rand.seed(42)

    trajectories = []

    for _ in range(number_of_trajectories):
        trajectory = []
        cumulative_sum = 0.0

        for _ in range(length_of_trajectory):
            random_number = pareto_distribution.gen_rand()
            cumulative_sum += random_number
            trajectory.append(cumulative_sum / (len(trajectory) + 1))

        trajectories.append(trajectory)

    return trajectories
