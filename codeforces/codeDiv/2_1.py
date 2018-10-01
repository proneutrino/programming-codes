n = input()
s =  raw_input().strip()
l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
k = ""
p = []
for i in s :
	if i not in l :
		#print i
		if i not in k :
			k += i 
	else :
		p.append(len(k)*(-1))
		k = ""
p.append(len(k)*(-1))
p.sort()
print p[0]*(-1)


