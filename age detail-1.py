# The program to get the user's age and get the exact time from seconds, hours, weeks, months, days...

# Creating the function and determining the formula of different values
def calculate_time(age):
    days = age * 365
    months = age * 12
    years = age
    weeks = age * 52
    hours = days * 24
    seconds = days * 24 * 60 * 60

    return days, months, years, weeks, hours, seconds
# Receive an input from the user and call them
age = int(input("Enter the age of the person: "))
days, months, years, weeks, hours, seconds = calculate_time(age)

# Print any formula
print(f"Number of days: {days}")
print(f"Number of months: {months}")
print(f"Number of years: {years}")
print(f"Number of weeks: {weeks}")
print(f"Number of hours: {hours}")
print(f"Number of seconds: {seconds}")