def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	return [[v * scalar for v in row] for row in matrix]