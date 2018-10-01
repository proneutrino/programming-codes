a,b,f,k = map(int,raw_input().split()) 
c = 0
td = k*a
e = b
p = 0
flag = 0
if f > b :
	print "-1"
else :
	while k > 1 :
		#print flag
		if p%2 == 0 :
			d = a
			d *= 2
			d -= f
			k -= 1
			p += 1
			if b >= d :
				td -= (a)
				b -= (a)

			else :
				if e >= d-f :
					b = e
					td -= (a)
					b -= (a-f)
					c += 1
				else :
					k = -1
					flag = 1
					break
		else :
			k -= 1
			p += 1
			if b >= a+f :
				td -= a
				b -= (a)
			else :
				if e >= 2*f :
					b = e
					td -= a
					b -= f
					c += 1
				else :
					k = -1
					flag = 1
					break
		#print flag
	
	if b < a :
		if p%2 == 0 and b < f:
			flag = 1
		else :
			if b<(f) :
				flag = 1

	if flag == 0 :
		print c
	else :
		print "-1"
