if __name__ == '__main__' :
	n = input()
	s = raw_input().strip()
	flag, i = 0, 0
	while i < n-1 :
		if s[i] != "?" and s[i] == s[i+1] :
			flag = 1
			break
		i += 1
	if flag == 1 :
		print "No"
	else :
		i = 0
		c = 0
		p = 0
		f = -1
		while i <= n :
			#print s[i]
			if i < n and s[i] == "?" :
				c += 1
				p += 1
			else :
				if f < c :
					f = c
				#print c, f
				c = 0
				
			i += 1
		
		if f == 1 :
			e = 0
			for i in range (n) :
				if s[i] == "?" :
					if i-1 >= 0 and i+1 < n and s[i-1] != s[i+1]:
						e += 1
			if e == p :
				print "No"
			else :
				print "Yes"

		else :
			print "Yes"


