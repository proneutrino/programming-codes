n, m = map(int, raw_input().split())
l = [0 for x in range (m+2)]
for _ in range (n) :
	e, r = map(int, raw_input().split())
	for i in range (e,r+1) :
		l[i] = 1

c = 0
for i in range (1, m+1) :
	if l[i] != 1 :
	 	c += 1

print c
for i in range (1, m+1) :
	if l[i] != 1 :
		print (i),

