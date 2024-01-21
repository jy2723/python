import random

attendance_status = random.randint(0, 2)
daily_wage = 20

if attendance_status == 1:
    print("Employee is Present")
    full_day = 8
    wage = daily_wage * full_day
    print("wage :",wage)
elif attendance_status == 2:
    part_time = 4
    parttime_wage = daily_wage * part_time
    print("parttime wage:", parttime_wage)
else:
    print("Employee is Absent")


