import matplotlib.pyplot as plt
import numpy as np

# ======= First Plot =======
# x = np.linspace(0, 10, 100)

# fig = plt.figure()

# plt.plot(x, np.sin(x), '-', label="sine")
# plt.plot(x, np.cos(x), '--', label="cosine")

# plt.xlabel("X axis label")
# plt.ylabel("Y axis label")

# plt.legend()
# plt.show()


# ======= Second Plot =======
# x = np.linspace(1, 5, 100)

# fig = plt.figure()

# plt.subplot(2, 1, 1)
# plt.plot(x, np.log(x), '-', label = "log")

# plt.subplot(2, 1, 2)
# plt.plot(x, np.exp(x), '--', label = "exp")

# plt.legend()
# plt.show()


# ======= Third Plot =======
# x = np.linspace(1, 5, 100)

# fig = plt.figure()
# fig.suptitle("Logs and Exps", fontsize=14)

# plt.subplot(1, 2, 1)
# plt.plot(x, np.log(x), '-', label = "log")

# plt.subplot(1, 2, 2)
# plt.plot(x, np.exp(x), '--', label = "exp")

# plt.legend()
# plt.show()


# ======= Fourth Plot =======
# x = np.linspace(1, 5, 100)
# fig = plt.figure()
# fig.suptitle("Logs and Exps", fontsize=20)

# plt.plot(x, np.log(x), '-', color = "green", label = "log")
# plt.plot(x, np.exp(x), '--', color = "red", label = "exp")


# plt.xlabel("X axis label")
# plt.ylabel("Y axis label")

# plt.legend()
# plt.show()


# ======= 3D Plot =======
# def f(x , y ) :
#     return np . sin ( x ) **2 + np . cos (1+ y * x ) * np . cos ( x )

# x = np.linspace (0 ,5 ,50)
# y = np.linspace (0 ,5 ,50)

# X , Y = np.meshgrid(x , y )
# Z = f(X, Y )

# fig = plt.figure ()

# ax = plt.axes ( projection = '3d')
# ax.contour3D (X, Y, Z, 50, cmap = 'binary')
# ax.set_xlabel ('x')
# ax.set_ylabel ('y')
# ax.set_zlabel ('z')

# plt.legend()
# plt.show()