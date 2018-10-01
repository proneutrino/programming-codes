if __name__ == '__main__' :
	kk = input()
	l = []
	for i in range (100000):
		k = str(i)
		s = 0
		for j in k :
			s += int(j)
		if s == 10 :
			l.append(-i)
		
		if (s-10) >= -9 and (s-10) < 0:
			t = i*10 + abs (10-s)
			if t not in l :
				l.append(-t)
	l.sort()
	print l[kk-1], len(l)
