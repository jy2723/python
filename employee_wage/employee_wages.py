import random

def present_case():
    print("Employee is Present\nwage:", daily_wage * 8)
    print("monthly wage :",daily_wage*8*20)

def part_time_case():
    print("parttime wage:", daily_wage * 4)
    print("monthly wage :",daily_wage*4*20)


def absent_case():
    print("Employee is Absent")

attendance_status = random.randint(0, 2)
daily_wage = 20


switch = {
    1: present_case,
    2: part_time_case,
    0: absent_case
}

switch.get(attendance_status, absent_case)()
