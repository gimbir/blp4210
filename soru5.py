# 5. Matplotlib kutuphanesi kullanarak: y=x2 , y=x, y = mutlak(x), y=sin(x) 2d grafiklerini çizdiren, meshgrid kullanarak z=x2+y2 grafiğini çizdiren kodu yazın.
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# Creating vectors X and Y
x = np.linspace(-5, 5, 255)
y = x ** 2

y2 = x

y3 = abs(x)

y4 = np.sin(x)

fig = plt.figure(figsize=(10, 8))

# Create the plot
plt.subplot(2, 2, 1), plt.plot(x, y), plt.title('y=x**2')
plt.subplot(2, 2, 2), plt.plot(x, y2), plt.title('y=x')
plt.subplot(2, 2, 3), plt.plot(x, y3), plt.title('y=|x|')
plt.subplot(2, 2, 4), plt.plot(x, y4), plt.title('y=sin(x)')

# z = x2 + y2
x0 = np.linspace(-10, 10, 25)
y0 = np.linspace(-10, 10, 25)

x, y = np.meshgrid(x0, y0)
z = (x ** 2) + (y ** 2)

cmap = plt.get_cmap('viridis')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap=cmap)
ax.set_title('z = x^2 + y^2')


plt.show()
