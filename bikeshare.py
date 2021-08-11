import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['all','january', 'february', 'march', 'april', 'may', 'june']
days = ['all','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
def get_filters():
    
    
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
   
        try :   
            city = str(input("Please enter a City name : ")).lower()
            if city in CITY_DATA.keys():
                break
            print("That is not a Valid City")
            print("Please enter one of these")
            for i in CITY_DATA.keys():
                print(" - "+i)
        except :
            pass
    
    while True:
        try :   
            month = str(input("Please enter a month or all ")).capitalize() 
            if month in months:
                break
            print("That is not a Valid month")
            print("Please enter one of these")
            for i in months:
                print(" - "+i)
        except :
            pass

    while True:
        try :   
            day = str(input("Please enter a week day or all : "))
            
            if day in days:
                break
            print("That is not a Valid day")
            print("Please enter one of these")
            for i in days:
                print(" - "+i)
        except :
            pass


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month == 'all':
        pass
    else:
        month = months.index(month)
        df = df[df['month'] == month]

    
    if day =='all':
        pass
    else:
        df = df[df['day_of_week'] == day.title()]
    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    popular_month=df['month'].mode()[0]
    print('Most Popular Month:',popular_month)
    
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:',popular_day)
    
    
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:',popular_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Popular Start Station:', popular_start_station)

    
    popular_end_station = df['End Station'].mode()[0]

    print('Most Popular End Station:', popular_end_station)

    
    df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
    popular_start_end_station = df['Start End'].value_counts().idxmax()
    print('Most Popular combination of start station and end station trip:', popular_start_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', travel_time)
    # TO DO: display mean travel time
    travel_mean = df['Trip Duration'].mean()
    print('Mean Travel Time:', travel_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    user_type = df['User Type'].value_counts()
    print('Counts of user types:', user_type)
    
    
    if 'Gender' in df.columns:
        user_gender = df['Gender'].value_counts()
        print('counts of gender:', user_gender)
    else:
        print("No Gender data Found in this dataset")
    
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print(f' - Earliest {earliest} \n - Most Recent {most_recent} \n - Most common {most_common}')
    else:
        print("No Birth Year data Found in this dataset")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
