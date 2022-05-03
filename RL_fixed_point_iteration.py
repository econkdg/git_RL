# ====================================================================================================
# fixed point iteration
# ====================================================================================================
# import library

import numpy as np
import matplotlib.pyplot as plt
# ----------------------------------------------------------------------------------------------------
# numerical approach

# computational thinking on how to calculate cos(x)=x
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.cos(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, linewidth=2)
plt.plot(x, x, linewidth=2)
plt.xlim(-2*np.pi, 2*np.pi)
plt.axvline(x=0, color='k', linestyle='--')
plt.axhline(y=0, color='k', linestyle='--')
plt.legend(['cos(x)', 'x'])
plt.axis('equal')
plt.ylim([-1, 1])

plt.show()

# naive approach
x = 0.3
print(np.cos(x))
print(np.cos(np.cos(x)))
print(np.cos(np.cos(np.cos(x))))
print(np.cos(np.cos(np.cos(np.cos(x)))))
print(np.cos(np.cos(np.cos(np.cos(np.cos(x))))))

# better way (1)
x = 0.3

for i in range(20):

    tmp = np.cos(x)
    x = np.cos(tmp)

print(x)

# better way (2)
x = np.zeros((30, 1))
x[0] = 0.3

for i in range(30-1):

    x[i+1] = np.cos(x[i])

print(x)

# better way (3)
x = 0.3

for i in range(30):

    x = np.cos(x)

print(x)

# use an idea of a fixed point
x = 2

for i in range(10):

    x = 2/x

    print(x)

x = np.linspace(-3, 3, 100)
y = 2/x

plt.figure(figsize=(8, 6))
plt.plot(x, y, linewidth=2)
plt.plot(x, x, linewidth=2)
plt.axvline(x=0, color='k', linestyle='--')
plt.axhline(y=0, color='k', linestyle='--')
plt.legend(['2/x', 'x'])
plt.axis('equal')
plt.ylim([-1, 1])

plt.show()

# how to overcome
# use an idea of a fixed point + kind of */damping/*
x = 3

for i in range(10):

    x = 1/2*(x + 2 / x)

print(x)

x = np.linspace(-4, 4, 100)
y = (x + 2/x)/2

plt.figure(figsize=(8, 6))
plt.plot(x, y, linewidth=2)
plt.plot(x, x, linewidth=2)
plt.axvline(x=0, color='k', linestyle='--')
plt.axhline(y=0, color='k', linestyle='--')
plt.axis('equal')
plt.ylim([-1, 1])

plt.show()
# ----------------------------------------------------------------------------------------------------
# system of linear equations

# matrix inverse (1)
A = np.array([[-4, -1, 1],
              [4, -8, 1],
              [-2, 1, 5]])

b = np.array([[7], [-21], [15]])

x = np.linalg.inv(A).dot(b)

# matrix inverse (2)
A = np.array([[-4, -1, 1],
              [4, -8, 1],
              [-2, 1, 5]])

b = np.array([[7], [-21], [15]])

A = np.asmatrix(A)
b = np.asmatrix(b)

x = A.I*b

# matrix inverse (3)
A = np.matrix([[-4, -1, 1],
               [4, -8, 1],
               [-2, 1, 5]])

b = np.matrix([[7], [-21], [15]])
b = np.matrix([7, -21, 15]).T

x = A.I*b

print(x)

# iterative way
A = np.array([[0, 1/4, -1/4],
              [4/8, 0, 1/8],
              [2/5, -1/5, 0]])

b = np.array([[7/4, 21/8, 15/5]]).T

x = np.array([[1, 1, 2]]).T  # initial point

A = np.asmatrix(A)
b = np.asmatrix(b)
x = np.asmatrix(x)

for i in range(20):

    x = A*x + b

print(x)

# think about why this one does not work
A = np.array([[3, 1, -1],
              [4, 7, 1],
              [2, -1, -4]])

b = np.array([[7, 21, 15]]).T

x = np.array([[1, 2, 2]]).T  # initial point

A = np.asmatrix(A)
b = np.asmatrix(b)
x = np.asmatrix(x)

for i in range(20):

    x = A*x + b

print(x)

# stability, check eigenvalue of A (1)
A = np.array([[3, 1, -1],
              [4, 7, 1],
              [2, -1, -4]])

np.linalg.eig(A)

# stability, check eigenvalue of A (2)
A = np.array([[3, 1, -1],
              [4, 7, 1],
              [2, -1, -4]])

np.linalg.eig(A)
# ----------------------------------------------------------------------------------------------------
# reference

# https://www.youtube.com/watch?v=xD7OCAjJ4TQ&list=PLGMtjo8jDX9CjkmQOEUSoY5QMVE-D86pK
# https://www.youtube.com/watch?v=EPhPj40wBs4&list=PLGMtjo8jDX9CjkmQOEUSoY5QMVE-D86pK&index=2
# ====================================================================================================
