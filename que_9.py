"""Q9.
Write a func that takes 3 args:
from_date - string representing a date in the form of 'yy-mm-dd'
to_date - string representing a date in the form of 'yy-mm-dd'
difference - int
Returns True if from_date and to_date are less than difference days away from each other, else
returns False."""

# Code 

from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    # Convert the date strings to datetime objects
    from_datetime = datetime.strptime(from_date, '%y-%m-%d')
    to_datetime = datetime.strptime(to_date, '%y-%m-%d')

    # Calculate the difference in days between the two dates
    date_difference = abs((to_datetime - from_datetime).days)

    # Check if the difference is less than the specified difference
    if date_difference < difference:
        return True
    else:
        return False

# Example usage
from_date = '21-05-10'
to_date = '21-05-15'
difference = 10

result = check_date_difference(from_date, to_date, difference)
print(result)
