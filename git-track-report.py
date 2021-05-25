#!/usr/bin/python3
import os
import time
from datetime import datetime

WEEKDAYS = {
    0: 'Mon',
    1: 'Tues',
    2: 'Weds',
    3: 'Thurs',
    4: 'Fri',
    5: 'Sat',
    6: 'Sun'
}

def print_working_hours(period):
    from_date = datetime.fromtimestamp(period['from'])
    to_date = datetime.fromtimestamp(period['to'])
    duration_hours = round((to_date - from_date).total_seconds()/3600, 2)
    return duration_hours

def get_time(log):
    return int(log[:10])

def build_working_hours():
    log_stream = os.popen('git log --pretty=format:"%ad %s" --date=raw --grep "hours:"')
    log_string = log_stream.read() 
    logs = log_string.split('\n')
    logs.sort(key=get_time)

    previous_time = 0
    working_hours = []
    for log in logs:
        if 'start' in log:
            previous_time = get_time(log)
            if log == logs[-1]:
                working_hours.append({
                    'from': previous_time,
                    'to': int(time.time())
                })
        elif 'stop' in log:
            working_hours.append({
                'from': previous_time,
                'to': get_time(log) 
            })
    return working_hours

def build_daily_hours(working_hours):
    daily_hours = {}
    for working_period in working_hours:
        day = datetime.fromtimestamp(working_period['from']).date()
        hours = print_working_hours(working_period)
        if day in daily_hours:
            daily_hours[day] += hours
        else:
            daily_hours[day] = hours
    return daily_hours

def build_weekly_hours(daily_hours):
    weekly_hours = {}
    for day in daily_hours:
        week = day.isocalendar()[1]
        if week not in weekly_hours:
            weekly_hours[week] = {}
        weekly_hours[week][WEEKDAYS[day.weekday()]] = round(daily_hours[day], 2)
    return weekly_hours

def total(week):
    total = 0
    for day in week:
        total += week[day]
    return round(total, 2)

def hours():
    working_hours = build_working_hours()
    daily_hours = build_daily_hours(working_hours)
    weekly_hours = build_weekly_hours(daily_hours)

    for week in weekly_hours:
        print('## Week {}'.format(week))
        for day in weekly_hours[week]:
            print('{}: {}'.format(day, weekly_hours[week][day]))
        print('Total: {}'.format(total(weekly_hours[week])))
        print('')

if __name__ == '__main__':
    hours()
