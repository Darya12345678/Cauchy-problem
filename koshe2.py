##интервал t = [0, 2]:

import numpy as np
import matplotlib.pyplot as plt

# задаем начальные условия
x0 = 3
vx0 = 1
y0 = -4
vy0 = 0

# задаем параметры системы
m = 1.0
L = 5.0

# задаем шаг по времени и интервал решения
dt = 0.01
t = np.arange(0, 2, dt)

# задаем функцию для переменного ускорения свободного падения
def g(t):
    return 9.81 + 0.05 * np.sin(2 * np.pi * t)

# создаем массивы для хранения решений
x = np.zeros_like(t)
vx = np.zeros_like(t)
y = np.zeros_like(t)
vy = np.zeros_like(t)

# задаем начальные значения
x[0] = x0
vx[0] = vx0
y[0] = y0
vy[0] = vy0

# решаем систему уравнений методом Эйлера
for i in range(1, len(t)):
    # вычисляем значения силы сопротивления стержня
    T = np.sqrt((m * g(t[i])) ** 2 - (m * np.sqrt(vx[i-1] ** 2 + vy[i-1] ** 2) / L) ** 2)

    # вычисляем значения проекций радиус-вектора груза
    x[i] = x[i-1] + vx[i-1] * dt
    y[i] = y[i-1] + vy[i-1] * dt

    # вычисляем значения скоростей груза
    vx[i] = vx[i-1] - x[i-1] / L * T * dt
    vy[i] = vy[i-1] - y[i-1] / L * T * dt - g(t[i-1]) * dt

# строим график
plt.plot(t, x**2 + y**2)
plt.xlabel('Time, s')
plt.ylabel('Distance, m')
plt.show()