import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if v1.shape != v2.shape:
		return -1
	if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
		return -1
	V = np.dot(v1,v2)
	mag1 = np.linalg.norm(v1)
	mag2 = np.linalg.norm(v2)
	cossine= (V/(mag1 * mag2))
	return cossine