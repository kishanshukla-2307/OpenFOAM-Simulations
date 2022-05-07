import csv
import math
import sys
import matplotlib.pyplot as plt

inputFile = sys.argv[1]

# innerFluid = []
# outerFluid = []
temperature_data = []
R1 = 0.00475
R2 = 0.00635
R3 = 0.014


with open(inputFile, newline='') as csvfile:
	data = csv.reader(csvfile, delimiter=' ', quotechar='|')
	print(data)
	for (i, row) in enumerate(data):
		if i == 0:
			continue
		row = [float(string) for string in row[0].split(",")]
		t, px, py, pz, id, bn = row
		temperature_data.append((px, py, pz, t))




dz = 0.0001    #thickness
# dr = 0.001    #ring thickness
length = 500    #length of pipe
no_of_points = int(length / dz)
# no_of_rings = int(R1 / dr)
# print("no_of_rings:", no_of_rings)

temperature = [[0, 0] for i in range(no_of_points + 1)]


for point in temperature_data:
	if point[2] > length or point[2] < 0:
		continue;

	z_index = int(point[2]/dz)
	temperature[z_index][0] += point[3]
	temperature[z_index][1] += 1

final_temperature = []

for (i, (t, n)) in enumerate(temperature):
	if n == 0:
		continue
	final_temperature.append(t / n)



with open(inputFile.split('.')[0] + ".txt", "w") as output_file:

    for temp in final_temperature:
    	output_file.write(str(temp) + "\n")

plt.plot(final_temperature)
plt.show()
