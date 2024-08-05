import datetime
def display_current_datetime():
    current_date = datetime.datetime.today()
    return current_date
print(f"Current date and time: {display_current_datetime()}")
days = int(input("Enter the number of days to add to the current date:"))
def calculate_future_date():
    future_date = datetime.date.today() + datetime.timedelta(days=days)
    print(f"Future date: {future_date}")
display_current_datetime()
calculate_future_date()