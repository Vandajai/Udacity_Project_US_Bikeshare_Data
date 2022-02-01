#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np


# In[2]:


CITY_DATA = { 'Chicago': 'chicago.csv',
              'new York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    


# In[3]:


# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

while True:
    city=input("\nWhich City you want to choose? Chicago/New York City/Washingtone\n:")
    if city not in ('Chicago','new York City','Washington'):
        print("Invalid input.Pls try again")
        continue
    else:
        break


# In[4]:


#TO DO: get user input for month (all, january, february, ... , june)
   
while True:
   month= input("\nWhich month you want to choose? January/February/March/April/May/June or type 'all' if no preference\n")
   if month not in ('January','February','March','April','May','May','June','all'):
       print("Invalid input.Pls try again")
       continue
   else:
       break
   


# In[5]:


#TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

while True:
    Day=input("\nWhich day you want to choose? Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday or 'all' if no preference\n")
    if Day not in ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','all'):
        print("Invalid input. Pls try again")
        continue
    else:
        break    


# In[6]:


print('-'*40)
print(city, month, Day)


# In[7]:


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


# In[27]:



#load data in to dataframe
df = pd.read_csv(r'.\ud_project\{}'.format(CITY_DATA[city]))
df


# In[9]:


# Change the start time & End Time format to date time format (yyyy-mm-dd)

df['Start Time']= pd.to_datetime(df['Start Time'])
df['End Time']=pd.to_datetime(df['End Time'])


# In[10]:


# extract month and day of the week from start time and create new column

df['month']=df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.weekday
print(df)


# In[11]:


#Filter by month 
#Defined variables

"""
    df         - City Dataframe
    time       - indicates the specified time (either "month", "day_of_month", or "day_of_week")
    month      - indicates the month used to filter the data
    week_day   - indicates the week day used to filter the data
    md         - list that indicates the month (at index [0]) used to filter the data
                    and the day number (at index [1])
"""

if time == 'month':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]


# In[12]:


# Filter by day of week

if time == 'day_of_week':
        days = ['Monday', 'Tuesday', 
        'Wednesday', 'Thursday', 
        'Friday', 'Saturday', 'Sunday','all']
        for d in days:
            if week_day.capitalize() in d:
                day_of_week = d
        df = df[df['day_of_week'] == day_of_week]
        
if time == "day_of_month":
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        month = md[0]
        month = months.index(month) + 1
        df = df[df['month']==month]
        day = md[1]
        df = df[df['day_of_month'] == day]
print(df)
    


# In[13]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time
    
    
# TO DO: display the most common month

popular_month=df['month'].mode()[0]
print("Most common month:", popular_month)


# In[14]:


# TO DO: display the most common day of week

popular_day= df['day_of_week'].mode()[0]
print("Most Common day of week: ", popular_day)


# In[15]:


# TO DO: display the most common start hour

df['hour']= df['Start Time'].dt.hour
popular_hour = df['hour'].mode()[0]
print("Most common hour:", popular_hour)


# In[16]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
# TO DO: display most commonly used start station
popular_start_station=df['Start Station'].value_counts().idxmax()
print("Most commonly used start station:",popular_start_station)


# In[17]:


# TO DO: display most commonly used end station

popular_end_station=df['End Station'].value_counts().idxmax
print("Most commonly used End station:", popular_end_station)
   


# In[18]:


# TO DO: display most frequent combination of start station and end station trip
   
combination_Station= df.groupby(['Start Station','End Station']).count()
print("combination of start and end station:", popular_start_station," & ",popular_end_station)


# In[19]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


# In[20]:


# TO DO: display total travel time

Total_travel_time = df['Trip Duration'].sum()/3600.0
print("Total travel time in hours:", Total_travel_time)


# In[21]:


# TO DO: display mean travel time

Total_mean_time = df['Trip Duration'].mean()/3600.0
print("Total travel time in hours:",Total_mean_time)


# In[ ]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


# In[25]:


# TO DO: Display counts of user types

user_types=df['User Type'].value_counts()
print("count of user_type:", user_types)


# In[24]:


# TO DO: Display counts of gender

if city !='Washington':
    try:
        gender_count= df['Gender'].value_counts()
        print("Count of gender:",gender_count)

    except keyError:
    
        print("No entry. Pls try again")


# In[23]:


# TO DO: Display earliest, most recent, and most common year of birth

try:
   Earliest_yearofbirth=df['Birth Year'].min()
   print("Most earliest year of birth:",Earliest_yearofbirth)
except keyError:
   print("No entry. Pls try again")
   
try:
   recent_yearofbirth=df['Birth Year'].max()
   print("Most recent year of birth:", recent_yearofbirth)
except keyError:
   print("No entry. Pls try again")
   
try:
   common_yearofbirth=df['Birth Year'].mode()
   print("Most common year of birth:",common_yearofbirth)
except keyError:
   print("No entry. Pls try again")


# In[ ]:


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

