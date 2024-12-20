import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import numpy as np

# Параметры системы Лоренца
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Функция, описывающая систему Лоренца
def lorenz(x, y, z, sigma, rho, beta):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

# Начальные условия
x0, y0, z0 = 0.0, 1.0, 1.05

# Временные параметры
dt = 0.01
num_steps = 10000

# Инициализация массивов для хранения значений
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Установка начальных значений
xs[0], ys[0], zs[0] = x0, y0, z0

# Численное интегрирование системы Лоренца
for i in range(num_steps):
    dx, dy, dz = lorenz(xs[i], ys[i], zs[i], sigma, rho, beta)
    xs[i + 1] = xs[i] + dx * dt
    ys[i + 1] = ys[i] + dy * dt
    zs[i + 1] = zs[i] + dz * dt

# Создание приложения PyQt5
app = QApplication(sys.argv)

# Создание главного окна
win = QMainWindow()
win.setWindowTitle('Аттрактор Лоренца')
win.setGeometry(100, 100, 800, 600)

# Создание графика с использованием pyqtgraph
plot_widget = pg.PlotWidget()
win.setCentralWidget(plot_widget)
plot_widget.showGrid(x=True, y=True)

# Добавление трехмерного графика
plot_item = plot_widget.plot(xs, ys, pen=pg.mkPen(color=(255, 0, 0), width=1))

# Отображение окна
win.show()
sys.exit(app.exec_())
