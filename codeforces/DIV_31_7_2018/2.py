n = input()
s = raw_input().strip()
t = raw_input().strip()
a, b = [], []
for i in range (26) :
	a.append(0)
	b.append(0)
for i in s :
	a[ord(i)-97] += 1
for j in t :
	b[ord(j)-97] += 1
flag = 0
for i in range (26) :
	if a[i] != b[i] :
		flag = 1
if flag == 1:
	print "-1"
elif s == t :
	print "0"
else :
	for i in range (n) :
		if s[i] == t[i] :
			continue
		else :
			for i in range ()

