import matplotlib.pyplot as plt
from math import cos, sin, pi
import random

theta = 60
velocity = 40

v = [velocity * cos(theta * pi / 180), velocity * sin(theta * pi / 180)]
g = -10
d = [0, 0]
d_list = [[0, 0]]

second = 0
n = 10

while True:
# for i in range(100):
    second += 1/n
    v[0] += random.uniform(-2, 2)
    v[1] += random.uniform(-2, 2)
    v[1] += g/n
    d[0] += v[0]/n
    d[1] += v[1]/n
    d_list.append(d.copy())
    if d[1] <= 0:
        break

print(d, second)
plt.scatter([i[0] for i in d_list], [i[1] for i in d_list])
temp = [i[0] for i in d_list] + [i[1] for i in d_list]
minimum = min(temp) - 20
maximum = max(temp) + 20
plt.xlim(minimum, maximum)
plt.ylim(minimum, maximum)
plt.show()