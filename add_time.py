def add_time(x, y, **kwargs):
    x = x.split()
    day = kwargs
    time_1 = x[0]
    (time_1_hour,
     time_2_hour,
     time_1_minute,
     time_2_minute) = time_1[:1:], y[:1:], time_1[2::], y[2::]

    add_hour = int(time_1_hour) + int(time_2_hour)
    add_minute = int(time_1_minute) + int(time_2_minute)
    if add_hour > 12:
        add_hour = 12 - add_hour
    if add_minute == 60:
        add_hour + 1
        add_minute = 0
    elif add_minute > 60:
        add_minute = 60 - add_minute

    print(f'{add_hour}:{add_minute} {x[1]}')



print(add_time("3:00 PM", "3:10"))