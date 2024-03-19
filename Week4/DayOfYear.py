from datetime import datetime

def day_of_year(date):
    # Parse the input date string
    parsed_date = datetime.strptime(date, '%Y-%m-%d')
    
    # Get the day of year
    day_of_year = parsed_date.timetuple().tm_yday
    
    return day_of_year

# Example usage
input_date = "2019-01-09"
day_number = day_of_year(input_date)
print("Day number of the year:", day_number)
