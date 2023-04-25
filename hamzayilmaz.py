import math
import random
import matplotlib.pyplot as plt

v = (330 + 1800) / 2.0
d = 20000
h = 50
L = 5000
n = 0
m = None
tempMin = 330
tempMax = 1800

while True:
    v = random.uniform(tempMin, tempMax) if m is not None else v
    theta = math.radians(30)

    g = 9.81
    s = 2 * v * math.sin(theta) / g
    m = v ** 2 * math.sin(2 * theta) / g

    if m <= d - L:
        print(f"onune dustu")
        tempMin = v
        n += 1
    elif m <= d + L:
        print(f"hedefi vurdun")
        break
    else:
        print(f"uzagina düstü")
        tempMax = v
        n += 1

print(f"{n}. seferde vuruş gerçekleştirmiştir. Hedefi vurmak için gerekli hız {v:.3f} m/s'tir.")

# vuruş koordinatını hesapla
t_max = 2 * v * math.sin(theta) / g
t = 0
dt = t_max / 100
x = []
y = []
while t <= t_max:
    x.append(v * math.cos(theta) * t)
    y.append(h + v * math.sin(theta) * t - 0.5 * g * t ** 2)
    t += dt

# grafiği çizdir
plt.plot(x, y)
plt.xlabel('Mesafe (m)')
plt.ylabel('Yükseklik (m)')
plt.title('Topun Vuruş Yolu')
plt.show()