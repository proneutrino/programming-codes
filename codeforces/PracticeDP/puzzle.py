if __name__ == '__main__' :
	n, m = map(int, raw_input().split())
	l = map(int, raw_input().split())
	l.sort()
	i = 0
	nn = n
	n -= 1
	s = 0
	f = 100000
	while i < m :
		if i+n < m :
			s = abs (l[i]-l[i+n])
		if f > s :
			f = s
		i += n

	if m%nn != 0 :
		r = m%nn
		j = m-1
		i = j-n
		while r != 0 :
			if i >= 0 and j >= 0 :
				s = abs (l[j]-l[i])
			#print l, l[i], l[j]
			if f > s :
				f = s
			j -= 1
			i -= 1
			r -= 1
			
	print f

