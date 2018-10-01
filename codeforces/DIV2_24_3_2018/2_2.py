def check(r, c, m) :
	for i in range (m) :
		if r[i] == c[i] and r[i] == "#":
			return 1
	return 0

if __name__ == '__main__' :
	n, m = map(int, raw_input().split()) 
	l = []
	for i in range (n) :
		l.append(raw_input().strip())

	f = 0
	for i in range (1) :
		r = l[i] 
		for j in range (i+1, n) :
			c = l[j]
			if check(r, c, m) == 1 :
				#print "j"
				for k in range (m) :
					if r[k] != c[k] :
						f = 1
	if f != 1 :
		print "Yes"
	else :
		print "No"
			
