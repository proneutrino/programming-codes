def minAmt(n, l, c, dp, cst, r) :
	if dp[n] != 10000000000 :
		if cst != 0 :
			dp[n] = min(dp[n], cst)
		return dp[n]
	if l <= 0 :
		return cst
	if n < 0  :
		return 10000000000

	x= min (minAmt(n, l-r[n], c, dp, cst+c[n], r), minAmt(n-1, l, c, dp, cst, r))
	dp[n] = min(x, dp[n])
	return dp[n]

if __name__ == '__main__' :
	n, l = map(int, raw_input().split())
	c = map(int, raw_input().split())
	r = []
	dp = []
	for i in range (n) :
		r.append(2**i)
	
	for i in range (n) :
		dp.append(10000000000)
	print minAmt(n-1, l, c, dp, 0, r)

