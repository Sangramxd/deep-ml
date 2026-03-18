def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a,b = matrix[0]
	c,d = matrix[1]
	trace = a + d
	det = (a*d)-(b*c)
	dis = trace ** 2 - 4*det
	l1 = (trace + dis**0.5)/2
	l2 = (trace - dis**0.5)/2
	return sorted([l1,l2], reverse=True)