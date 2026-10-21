count_time = 0
times = '1h 45m,360s,25m,30m 120s,2h 60s'

lst = times.split(',')

for time in lst:
    if 'h' in time:
        hours_str = time.split('h')[0]
        count_time += int(hours_str) * 60

    if 'm' in time:
        minutes_str = time.split('m')[0]
        minutes_str = minutes_str.replace('h', '')
        minutes_str = minutes_str.split()[-1]
        count_time += int(minutes_str)

    if 's' in time:
        seconds_str = time.split('s')[0]
        seconds_str = seconds_str.replace('m', '')
        seconds_str = seconds_str.replace('h', '')
        seconds_str = seconds_str.split()[-1]
        count_time += int(seconds_str) // 60

print(count_time)