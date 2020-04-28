import psutil as ps
import datetime as dt
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,4))
x1, x2, x3, y1, y2, y3 = [], [], [], [], [], []
while (True):
    timeStr = str(dt.datetime.now())
    current_time = dt.datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S.%f')
    # hour = now.hour
    # minute = now.minute
    # second = now.second
    cpu_p = int(ps.cpu_percent())
    mem_p = int(ps.virtual_memory().percent)
    disk_p = int(ps.disk_usage('/').percent)
    x1.append(current_time)
    x2.append(current_time)
    x3.append(current_time)
    y1.append(cpu_p)
    y2.append(mem_p)
    y3.append(disk_p)
    # y = cpu_p
    # x = second
    # y = cpu_p
    line1 = plt.plot(x1, y1, linestyle='-', c='b', marker='o')
    line2 = plt.plot(x2, y2, linestyle='-', c='r', marker='o')
    line3 = plt.plot(x3, y3, linestyle='-', c='g', marker='o')
    # plt.plot(y, 'ro')
    plt.xlabel('Time')
    plt.ylabel('Percentage(%)')
    plt.title('PC Resource Monitoring')
    plt.pause(1)

plt.legend()
# plt.legend(handles=(line1, line2, line3), labels=('CPU', 'Memory', 'Disk'))
plt.show()