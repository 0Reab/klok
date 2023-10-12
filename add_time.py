import re
def add_time(x, y, **kwargs):
    day = kwargs
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
        if AM == True:
            AM = False
        else:
            AM == True


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

    print(f'{add_hr}:{add_min} {time_of_day}')



print(add_time("11:00 AM", "24:00"))