import re
def add_time(x, y, day=""):
    week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    day_count = 0
    temp_list1 = re.split(':| ', x)
    temp_list2 = re.split(':| ', y)

    hr1 = temp_list1[0]
    min1 = temp_list1[1]

    if temp_list1[2] == "AM":
        AM = True
        PM = False
    else:
        temp_list1[2] != "AM"
        AM = False
        PM = True

    hr2 = temp_list2[0]
    min2 = temp_list2[1]

    add_hr = int(hr1) + int(hr2)
    add_min = int(min1) + int(min2)

    while add_hr > 12:
        add_hr = add_hr - 12
        day_count = float(day_count) + 0.5

        if AM == True:
            AM = False

        else:
            AM = True

    if add_min == 60:
        add_hr = add_hr + 1
        add_min = 00

    while add_min > 60:
        add_hr = add_hr + 1
        add_min = add_min - 60


    if AM == True:
        time_of_day = "AM"
    else:
        time_of_day = "PM"


    if day != "":
        for i in week:
            if i in week == day:
                if day_count == 1:
                    print(f'{add_hr}:{add_min} {time_of_day}, {i} (next day)')
                if day_count < 1:
                    print(f'{add_hr}:{add_min} {time_of_day}, {i}')
                else:
                    day_count > 1
                    print(f'{add_hr}:{add_min} {time_of_day}, {i} ({day_count} days later)')

# if statmenti i loop ne rade kako treba
# am_pm ne radi u ovom slucaju inputa "11:43 AM", "00:20"

    if day == "":
        for i in week:
            if day_count == 1:
                print(f'{add_hr}:{add_min} {time_of_day} (next day)')
            if day_count < 1:
                print(f'{add_hr}:{add_min} {time_of_day}')
            else:
                day_count > 1
                print(f'{add_hr}:{add_min} {time_of_day} ({day_count} days later)')

    # else:
    #     print(f'{add_hr}:{add_min} {time_of_day}')
#TEST CASES

# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM
# add_time("11:30 AM", "2:32", "Monday")
# # Returns: 2:02 PM, Monday
# add_time("11:43 AM", "00:20")
# # Returns: 12:03 PM
# add_time("10:10 PM", "3:30")
# # Returns: 1:40 AM (next day)
# add_time("11:43 PM", "24:20", "tueSday")
# # Returns: 12:03 AM, Thursday (2 days later)
# add_time("6:30 PM", "205:12")
# # Returns: 7:42 AM (9 days later)
print(add_time("6:30 PM", "205:12"))