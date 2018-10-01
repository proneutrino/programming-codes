p = ""
def mini (x, y) :
	if x != -1 and y != -1 :
		return min(x,y)
	if  x == -1 :
		return y
	else :
		return x

def count (n, i, dp, c, l, p) :
	
	if n == 0 :
		return c
	if n < 0 or i >= 64:
		return -1
	
	if dp[n] != -1 :
		return dp[n]

	dp[n] = mini(count(n, i+1, dp, c, l, p), count(n-l[i], i, dp, c+1, l, p + str(l[i])))
	return dp[n]


if __name__ == '__main__':
	n = input()
	dp, l = [], []
	for i in range (1, 1000001) :
		if "2" not in str(i) and "3" not in str(i) and "4" not in str(i) and "5" not in str(i) and "6" not in str(i) and "7" not in str(i) and "8" not in str(i) and "9" not in str(i):
			l.append(i)
		dp.append(-1)
	
	
	
	s = ""
	a = []
	while  n > 0:
		N, m, p = n, 0, 1
		
		while N > 0:
			if N%10 > 0:
				m += p
			N /= 10
			p *= 10
				#print m, p, N
			
		
		a.append(m)
		n -= m
		

	a.sort()
	print len(a)
	for i in a :
		s += str(i) + " "
	print s
    
	#print count (n)