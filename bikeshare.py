import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        #make capital letter input to lower letter to avoid errors
        city = input("Choose a city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA.keys(): break
        print("Wrong input! You must choose from 'Chicago', 'New York City', or 'Washington'.")
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        #make capital letter input to lower letter to avoid errors
        month = input("Choose month (all, january, ... , june): ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']: break
        print("Wrong input! You must choose from 'all', 'january', 'february', 'march', 'april', 'may', or 'june'.")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        #make capital letter input to lower letter to avoid errors
        day = input("Choose day of week (all, monday, tuesday, ... ,sunday): ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']: break
        print("Wrong input! You must choose from 'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'.")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    # TO DO: display the most common day of week
    df['Day of week'] = df['Start Time'].dt.weekday
    common_day_of_week = df['Day of week'].mode()[0]
    print('Most common day of week:', common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station:', common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common end station:', common_start_station)
    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).idxmax()
    print('Most common start and end station trip:', common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(gender)
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_birth = df['Birth Year'].min()
        print('Earliest year of birth: ', earliest_year_birth)
        recent_year_birth = df['Birth Year'].max()
        print('Most recent year of birth: ', recent_year_birth)
        most_common_year_birth = df['Birth Year'].mode()[0]
        print('Most common year of birth: ', most_common_year_birth)
    except:
        print('Washington does not have gender and birth year data.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#show raw data by five lines
def display_five_row(df):
    raw_data = input('Would you like to see the raw data? ', ).lower()
    if raw_data == 'yes':
        i = 0
        #use while loop to ask whether they wants to see 5 more rows
        while True:
            print(df.iloc[i:i+5, :])
            i = i + 5
            five_more_raws = input('Would you like to see five more rows? ').lower()
            if five_more_raws != 'yes': break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_five_row(df)
        #ask whether to start over
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
