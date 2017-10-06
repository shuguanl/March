import numpy as np
import matplotlib.pyplot as plt

words = ["I", "like", "deep", "enjoy", "deep", "learning", "NLP", "flying"]

x = np.array([[0, 2, 1, 0, 0, 0, 0, 0],
              [2, 0, 0, 1, 0, 1, 0, 0],
              [1, 0, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 1],
              [0, 1, 0, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 1, 1, 1, 0]])

U, s, Vh = np.linalg.svd(x, full_matrices = False);

print(U)

plt.xlim([-1, 1])
plt.ylim([-1, 1])

for i in range(len(words)) :
    print("[{0:.2f}, {1:.2f}]{2}".format(U[i,0], U[i,1], words[i]))
    plt.text(U[i, 1], U[i, 2], words[i])
plt.show()

        