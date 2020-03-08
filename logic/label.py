import numpy as np

def encode_label(j):
	e = np.zeros((10, 1))
	e[j] = 1.0
	return e

print(encode_label(1))