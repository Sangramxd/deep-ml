def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	col_a = len(a[0])
	row_b = len(b)
	if col_a != row_b:
		return -1
	results = []
	for i in range(len(a)):
		row = []
		for j in range(len(b[0])):
			val =0
			for k in range(len(a[0])):
				val += a[i][k] * b [k][j]
			row.append(val)
		results.append(row)
	return results