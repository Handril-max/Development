
def add_time(start, duration, start_day=None):
    # Parse start time
    start_time, period = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))

    # Parse duration time
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Convert start time to 24-hour format
    if period == 'PM' and start_hours != 12:
        start_hours += 12

    # Calculate total minutes in start time
    total_start_minutes = start_hours * 60 + start_minutes

    # Calculate total minutes in duration time
    total_duration_minutes = duration_hours * 60 + duration_minutes

    # Calculate total minutes after adding duration time
    total_minutes = total_start_minutes + total_duration_minutes

    # Calculate new hours and minutes
    new_hours = total_minutes // 60 % 24
    new_minutes = total_minutes % 60

    # Calculate new time period
    if new_hours < 12:
        new_period = 'AM'
    else:
        new_period = 'PM'
        if new_hours > 12:
            new_hours -= 12

    # Calculate number of days to add
    days = total_minutes // 1440

    # Calculate new day of the week
    weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    new_day = ''
    if start_day:
        start_day = start_day.lower()
        start_day_index = weekdays.index(start_day)
        new_day_index = (start_day_index + days) % 7
        new_day = ', ' + weekdays[new_day_index].capitalize()

    # Generate formatted output string
    result = f"{new_hours:02d}:{new_minutes:02d} {new_period}"
    if start_day:
        result += new_day
    if days == 1:
        result += ' (next day)'
    elif days > 1:
        result += f' ({days} days later)'

    return result


print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))