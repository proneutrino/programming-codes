if __name__ == '__main__' :
	n, m = map(int, raw_input().split())
	l, r, c = [], [], []
	for i in range (n) :
		l.append(raw_input().strip())

	for i in range (n) :
		r.append(0)

	for i in range (m) :
		c.append(0)

	p, tot = 0, 0

	for i in range (n) :
		for j in range (m) :
			if l[i][j] == "#" :
				tot += 1
	for i in range (n) :
		if r[i] != 1 :
			for j in range (m) :
				if c[j] != 1 and l[i][j] == "#" :
					for k in range (i,n) :
						if l[k][j] == "#" :
							r[k] = 1
							p += 1
					c[j] = 1
	if p == tot :
		print "Yes"
	else :
		print "No"
for i in range (n) :
	for j in range (m) :
		if l[i][j] == "#" :
			for k in range (i,n) :
				if 
				for t in range (m) :
					if l[i][j] == l[]




