if __name__ == '__main__' :
	n = input()
	l = map(int, raw_input().split())
	s, c = 1, 0
	for i in range (n-1) :
		if l[i] <= l[i+1] :
			if i+1 == n-1 :
				c += 2
			else :
				c += 1
		else :
			c += 1
			if s < c :
				s = c
			c = 0
	if s > c :
		print s
	else :
		print c

