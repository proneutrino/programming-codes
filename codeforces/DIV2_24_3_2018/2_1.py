if __name__ == '__main__' :
	n, m = map(int, raw_input().split())
	l = []
	for i in range (n) :
		l.append(raw_input().strip())
	f = 0
	for i in range (1) :
		r = l[i]
		tot = 0
		for u in r :
			if u == "#" :
				tot += 1
		for j in range (i+1, n) :
			c = 0
			for k in range (m) :
				if r[k] == l[j][k] and r[k] == "#" :
					c += 1
			if c >= 1 and c != tot :
				#print "No"
				f = 1
			print c, f
	if f == 0 :
		print "Yes"
	if f == 1 :
		print "No"
