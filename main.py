import numpy as np
import matplotlib.pyplot as plt

# 1. Гистограмма
mean = 0
std_dev = 1
num_samples = 1000
data = np.random.normal(mean, std_dev, num_samples)
plt.hist(data, bins=30)
plt.title("Гистограмма нормального распределения")
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.grid(True)
plt.show()

# 2. Диаграмма рассеяния
x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y, color='blue', alpha=0.5)
plt.title("Диаграмма рассеяния случайных данных")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()