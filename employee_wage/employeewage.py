import random

def calculate_daily_wage(hours_worked, daily_wage):
    return daily_wage * hours_worked

def calculate_monthly_wage(daily_wage, hours_per_day, days_per_month):
    return daily_wage * hours_per_day * days_per_month

def calculate_wages(target_hours, target_days, daily_wage, hours_per_day):
    total_hours_worked = 0
    total_days_worked = 0

    while total_hours_worked < target_hours and total_days_worked < target_days:
        attendance_status = random.randint(0, 2)

        if attendance_status == 1:  
            hours_worked_today = 8  
            total_hours_worked += hours_worked_today
            total_days_worked += 1

        elif attendance_status == 2:  
            hours_worked_today = 4  
            total_hours_worked += hours_worked_today
            total_days_worked += 1

        else:  
            pass
    total_wages = calculate_monthly_wage(daily_wage, hours_per_day, total_days_worked)
    print(f"\nTotal Hours Worked: {total_hours_worked}")
    print(f"Total Days Worked: {total_days_worked}")
    print(f"Total Wages: {total_wages}")

target_hours = 100
target_days = 20
daily_wage = 20
hours_per_day = 8

calculate_wages(target_hours, target_days, daily_wage, hours_per_day)
