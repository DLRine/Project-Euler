def r():
	n = 2**1000
	ans = sum(int(c) for c in str(n))
	return str(ans)
r = r()
print(r)