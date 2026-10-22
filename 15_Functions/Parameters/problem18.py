def convert_minutes(minutes, seconds_per_minute=60):
    return minutes * seconds_per_minute


print(convert_minutes(5))
print(convert_minutes(5, 60))
