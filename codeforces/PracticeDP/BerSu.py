if __name__ == '__main__' :
	n = input()
	b = map(int, raw_input().split())
	m = input()
	g = map(int, raw_input().split())
	b.sort()
	g.sort()
	c = 0
	for i in b :
		for j in range (m) :
			if g[j] != -1 and abs(i-g[j]) <= 1 :
				#print g[j], i
				g[j] = -1
				c += 1
				break
	print c
