n = input()
s = raw_input().strip()
c = 0
l = []
for i in s :
	if i >= 'A' and i <= 'Z' :
		c += 1
	if i == ' ':
		l.append(c)
		c = 0
l.append(c)
l.sort()
print l[len(l)-1]
