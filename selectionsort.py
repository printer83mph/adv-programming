def selectionsort(list):
	inp = list
	out = []
	while len(inp) > 0:
		minn = inp[0]
		index = 0
		for i in range(len(inp)):
			if inp[i] < minn:
				index = i
				minn = inp[i]
		out.append(inp.pop(index))
	return out

print selectionsort([5,2,8,4])
