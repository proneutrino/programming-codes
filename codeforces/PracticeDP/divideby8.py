def rec(x, l, i, n, dp) :
	if x%8 == 0 and x != 0:
		return x
	if i >= n :
		return 0
	if dp[x%8][i] != -1 :
		#print dp[x%8][i]
		return dp[x%8][i]

	dp[x%8][i] = max(rec(x*10+l[i], l, i+1, n, dp),rec(x, l, i+1, n, dp));
	return dp[x%8][i]


n = raw_input().strip()
l = []
for i in n :
	l.append(int(i))

dp = []
for i in range (105) :
	r = []
	for i in range (105) :
		r.append(-1)
	dp.append(r)

x = rec(0, l, 0, len(n), dp)
if 0 in l :
	print "YES"
	print "0"
elif x != 0 :
	print "YES"
	print x
else :
	print "No"