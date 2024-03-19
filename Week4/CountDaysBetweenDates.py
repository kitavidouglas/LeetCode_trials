from datetime import datetime

def count_days(date1, date2):
    # Parse the input date strings into datetime objects
    datetime1 = datetime.strptime(date1, "%Y-%m-%d")
    datetime2 = datetime.strptime(date2, "%Y-%m-%d")

    # Calculate the difference between the two dates in terms of days
    days_difference = abs((datetime2 - datetime1).days)

    return days_difference

# Example usage
date1 = "2019-06-29"
date2 = "2019-06-30"
print("Number of days between the two dates:", count_days(date1, date2))  # Output: 1
