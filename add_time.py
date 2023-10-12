import re
def add_time(x, y, **kwargs):
    day = kwargs
    temp_list1 = re.split(':| ', x)
    temp_list2 = re.split(':| ', y)

    hr1 = temp_list1[0]
    min1 = temp_list1[1]
    am_pm = temp_list1[2]

    hr2 = temp_list2[0]
    min2 = temp_list2[1]

    add_hr = int(hr1) + int(hr2)
    add_min = int(min1) + int(min2)

    if add_hr > 12:
        add_hr = add_hr - 12
        if am_pm == "AM":
            am_pm = "PM"
        else:
            am_pm = "AM"


    print(f'{add_hr}:{add_min} {am_pm}')



print(add_time("11:43 AM", "2:20"))