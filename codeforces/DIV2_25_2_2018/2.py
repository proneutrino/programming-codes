import math

def wait (h, l) :
	e = int(math.sqrt (h))
	for i in range (2,e+1) :
		if i <= l and h%i == 0 and h/i != 1:
			return 0
		if i > l :
			return h
	return h

p, y = map(int, raw_input().split())
if p+1 == y :
	print "-1"
else :
	l = p+2
	h = y-1
	lfag = 0
	while h >= l :
		k = wait (h, p+1) 
		if k != 0 :
			print k
			lfag = 1
			break
		h -= 1
	if lfag == 0 :
		print "-1"
