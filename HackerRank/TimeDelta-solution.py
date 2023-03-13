from datetime import datetime
date_strftime = '%a %d %b %Y %H:%M:%S %z'
a = []
count = input()
for i in range(int(count)):
    start = input()
    end = input()
    a.append(abs(
        datetime.strptime(end, date_strftime) -
        datetime.strptime(start, date_strftime)).total_seconds())
for i in range(int(count)):
    print(int(a[i]))
