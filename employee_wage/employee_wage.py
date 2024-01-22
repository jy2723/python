import random

def calculate_daily_wage(hours_worked, daily_wage):
    return daily_wage * hours_worked

def calculate_monthly_wage(daily_wage, hours_per_day, days_per_month):
    return daily_wage * hours_per_day * days_per_month

def present_case():
    print("Employee is Present\nWage:", calculate_daily_wage(8, daily_wage))
    print("Monthly Wage:", calculate_monthly_wage(daily_wage, 8, 20))

def part_time_case():
    print("Part-time wage:", calculate_daily_wage(4, daily_wage))
    print("Monthly Wage:", calculate_monthly_wage(daily_wage, 4, 20))

def absent_case():
    print("Employee is Absent")

attendance_status = random.randint(0, 2)
daily_wage = 20

if attendance_status == 1:
    present_case()
elif attendance_status == 2:
    part_time_case()
else:
    absent_case()
