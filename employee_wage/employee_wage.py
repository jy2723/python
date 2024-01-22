import random

def calculate_wage(attendance_status, daily_wage):
    if attendance_status == 1:
        return full_day_wage(daily_wage)
    elif attendance_status == 2:
        return part_time_wage(daily_wage)
    else:
        return 0

def full_day_wage(daily_wage):
    full_day_hours = 8
    return daily_wage * full_day_hours

def part_time_wage(daily_wage):
    part_time_hours = 4
    return daily_wage * part_time_hours

def main():
    attendance_status = random.randint(0, 2)
    daily_wage = 20

    if attendance_status == 1:
        print("Employee is Present")
    elif attendance_status == 2:
        print("Employee is Part-Time")
    else:
        print("Employee is Absent")

    wage = calculate_wage(attendance_status, daily_wage)
    print("Wage:", wage)

if __name__ == "__main__":
    main()
