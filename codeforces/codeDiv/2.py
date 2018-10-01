n = input()
s = raw_input().strip()
l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
k = ""
p = []
i = 0
#print s
while i < n:
	print k
	if s[i] in l :
		for j in range (i+1,n) :
			if s[j] in l :
				break
			else :
				if s[j] not in k :
					k += s[j]
				else :
					p.append(len(k)*(-1))
					k = ""
		i = j
	else :
		i += 1

p.sort()
print p[0]*(-1)
