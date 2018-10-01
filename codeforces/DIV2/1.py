n,k = map(int,raw_input().split())
s = raw_input().strip()
flag = 0
l = []
sm = 0
e = "abcdefghijklmnopqrstuvwxyz"
for i in e :
	l.append (s.count(i))
while k != 0 :
	for i in range (26) :
		if l[i] != 0 :
			sm += 1
			l[i] -= 1;
	if sm == n :
		flag = 1
		break
	k -= 1
if flag == 0 :
	print "NO"
else :
	print "YES"
