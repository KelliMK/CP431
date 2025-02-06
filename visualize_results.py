import matplotlib.pyplot as plt

pros = [2, 3, 4, 5, 6, 7, 8]
times = [242.22514033,159.32884526,120.54280782,98.57572269,82.38693213,71.67383671, 63.71252036]

plt.plot(pros, times, marker="o")
plt.xlabel("# of Processors")
plt.ylabel("Run Time (seconds)")
plt.title("Assignment 1 Program Benchmarks")
plt.show()