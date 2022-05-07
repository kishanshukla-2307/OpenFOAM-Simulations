import csv
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import sys

X = []
Y = []
Z = []
MAX_VELOCITY = 0.1
R1 = 0.00475
R2 = 0.00635
R3 = 0.014
inputFile = sys.argv[1]
outputFile = sys.argv[2]
outer = sys.argv[3]
count = 0
maxR = 0
with open(inputFile, newline='') as csvfile:
	data = csv.reader(csvfile, delimiter=' ', quotechar='|')
	print(data)
	for (i, row) in enumerate(data):
		if i == 0:
			continue
		x = float(row[0].split(',')[0])
		y = float(row[0].split(',')[1])
		z = float(row[0].split(',')[2])
		X.append(x)
		Y.append(y)
		Z.append(z)
		maxR = max(maxR, math.sqrt(x**2 + y**2))
		# if math.sqrt(x**2 + y**2) > R1:
		# 	print(x, y, math.sqrt(x**2 + y**2))
		# 	count += 1

print(count)
np_X = np.array(X)
np_Y = np.array(Y)
np_Z = np.array(Z)


r = np.abs(np.sqrt(np.add(np.power(np_X, 2), np.power(np_Y, 2))))
R = maxR
# for outer velocity
if (int(outer) == 1):
	r = np.subtract(r, (R2 + R3)/2)
	R = (R3 - R2)/2
	MAX_VELOCITY = 0.01


Uz = np.multiply(np.subtract(np.ones(r.shape), np.power(np.divide(r, R), 2)), MAX_VELOCITY)
print(Uz.shape)

with open(outputFile, "w") as file:
	for uz in Uz:
		file.write("(0 0 " + str("{:.4f}".format(uz)) + ")\n")



fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(np_X, np_Y, Uz)
ax.set_title(r'$\mathregular{U_z}$ vs (x, y)')
ax.set_xlabel('$X$', rotation=0)
ax.set_ylabel('$Y$')
ax.set_zlabel(r'$\mathregular{U_z}$', rotation=0)
plt.show()
