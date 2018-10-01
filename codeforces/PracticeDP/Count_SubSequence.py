def subsequence (l, s) :
	m, n = len(l), len(s)
	dp, r = [], []
	for i in range (m+1) :
		for j in range (n+1) :
			r.append(0)
		dp.append (r)
	for i in range (m) :
		dp[i][0] = 1
	for i in range (1,m+1) :
		for j in range (1,n+1) :
			if l[i-1] == s[j-1] :
				dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
			else :
				dp[i][j] = dp[i-1][j]
	return dp[m][n]
if __name__ == '__main__' :
	l = raw_input().strip()
	s = "QAQ"
	print subsequence(l, s)
