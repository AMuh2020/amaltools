import datetime
import time

def date_to_unix(date_string, date_format="%Y-%m-%d"):
    dt = datetime.datetime.strptime(date_string, date_format)
    unix_time = time.mktime(dt.timetuple())
    return int(unix_time)

# print(date_to_unix("2022-01-01"))  # 1640995200

def unix_to_date(unix_time, date_format="%Y-%m-%d"):
    dt = datetime.datetime.fromtimestamp(unix_time)
    return dt.strftime(date_format)

# print(unix_to_date(1640995200))  # 2022-01-01

def get_current_unix_time():
    return int(time.time())

print(get_current_unix_time())

def unix_to_discord_time(unix_time):
    return f"<t:{unix_time}:F>"

