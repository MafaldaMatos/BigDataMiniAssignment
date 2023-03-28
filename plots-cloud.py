import matplotlib.pyplot as plt
import numpy as np

seqpy = np.array([102])
beam = np.array([3.9,37.6,46.6,253.9])

memorybeam = np.array([31.1,195.9,438.5,1400])
memoryseq = np.array([31.3])

plt.scatter(memoryseq, seqpy, color = 'g', label="Sequential")
plt.plot(memorybeam, beam, color = 'r', label="Beam")
plt.title("Efficiency of Different Code Implementations")
plt.xlabel("Dataset Size (MB)")
plt.ylabel("Time (s)")
plt.legend()

plt.savefig('plot-cloud.png')
