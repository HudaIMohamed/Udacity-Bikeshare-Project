import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

days = ['saturday',  'sunday',  'monday',  'tuesday',  'wednesday',  'thursday',  'friday', 'all']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

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
        city = input('Enter a city. Choose between Chicago, New York City, Washington or all: ')
        if city not in CITY_DATA:
            print('Pleas enter a valid input. Check your spelling and pick one of the three cities available or enter "all": ')
            continue
        else:
            break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter a month from Jan to June or "all" for viewing data from all set of months: ')
        if month not in months:
            print('Make sure to enter a month from a Jan to June: ')
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter your day of choice or "all" for viewing data from all weekdays: ')
        if day not in days:
            print('Invalid input. Check your spelling and enter a day name, its abbreviation form, or enter "all": ')
            continue
        else:
            break


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
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Weekday'] == day.title()]

    return df

def time_stats(df):
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    freq_month = df['Month'].mode()[0]
    months = {1:'Jan', 2:'Feb', 3:'Mar', 4:'April', 5:'May', 6:'June'}
    freq_month_name = months[freq_month]
    print('The month with the highest rate of customers is {}'.format(freq_month_name))
    
    freq_day = df['Weekday'].mode()[0]
    print('Most common weekday is {}'.format(freq_day))

    df['Hour'] = df['Start Time'].dt.hour
    freq_hour = df['Hour'].mode()[0]
    print('Most common hour of the day is {}'.format(freq_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_visited_start = df['Start Station'].mode()[0]
    print('Most commonly used start station is {}'.format(most_visited_start))   

    # TO DO: display most commonly used end station
    most_visited_end = df['End Station'].mode()[0]
    print('Most commonly used end station is {}'.format(most_visited_end))

    # TO DO: display most frequent combination of start station and end station trip
    common_combination = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('Most common combination of start and end stations is {}'.format(common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is {}'.format(total_travel_time))

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average of travel time is {}'.format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)  

def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('Count of each user type is: {}'.format(user_types_count))

    # TO DO: Display counts of user types
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print('Count of each gender is: {}'.format(gender))
        oldest_customer = df['Birth Year'].min()
        print('Oldest customer was born in {}'.format(oldest_customer))
        youngest_customer = df['Birth Year'].max()
        print('Youngest customer was born in {}'.format(youngest_customer))
        most_common_age = df['Birth Year'].mode()
        print('Most common birth year among customers is {}'.format(most_common_age))
    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_dat(df):
    
    while True:
        more_data = input('Would you like to view more data? answer with yes or no: ')
        if more_data != 'no':
            print(df.iloc[:,+5])
        else:
            break        
           
    return df
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_dat(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()