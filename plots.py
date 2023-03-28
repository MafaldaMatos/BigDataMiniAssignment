import matplotlib.pyplot as plt
import numpy as np

seqpy = np.array([67.4])
pyspark = np.array([7.5,8.4,7.6,7.9,7.5,9,9.2])
beam = np.array([2,29.6,34.8,191.3,255.9,186.2])

memorybeam = np.array([31.1,195.9,438.5,1400,1600,1800])
memoryspark =  np.array([31.1,195.9,438.5,778,1400,1600,1800])
memoryseq = np.array([31.3])

plt.scatter(memoryseq, seqpy, color = 'g', label="Sequential")
plt.plot(memoryspark, pyspark, color = 'b', label="Pyspark")
plt.plot(memorybeam, beam, color = 'r', label="Beam")
plt.title("Efficiency of Different Code Implementations")
plt.xlabel("Dataset Size (MB)")
plt.ylabel("Time (s)")
plt.legend()

plt.savefig('plot.png')
