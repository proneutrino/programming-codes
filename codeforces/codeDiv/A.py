a,b = raw_input().split()
n = input()
if a == '^' :
	if b == '>' :
		if n%4 == 1 :
			print 'cw'
		elif n%4 == 3 :
			print 'ccw'
	elif b == '<' :
		if n%4 == 1 :
			print 'ccw'
		elif n%4 == 3 :
			print 'cw'
	elif b == 'v' or b == '^':
		print 'undefined'
elif a == '>' :
	if b == '^' :
		if n%4 == 1 :
			print 'ccw'
		elif n%4 == 3 :
			print 'cw'
	elif b == '<' or b == '>' :
		print 'undefined'
	elif b == 'v' :
		if n%4 == 1 :
			print 'cw'
		elif n%4 == 3 :
			print 'ccw'
elif a == '<' :
	if b == '^' :
		if n%4 == 1 :
			print 'cw'
		elif n%4 == 3 :
			print 'ccw'
	elif b == '>' or b == '<' :
		print 'undefined'
	elif b == 'v' :
		if n%4 == 1 :
			print 'ccw'
		elif n%4 == 3 :
			print 'cw'
elif a == 'v' :
	if b == '^' or b == 'v' :
		print 'undefined'
	elif b == '>' :
		if n%4 == 1 :
			print 'ccw'
		elif n%4 == 3 :
			print 'cw'
	elif b == '<' :
		if n%4 == 1 :
			print 'cw'
		elif n%4 == 3 :
			print 'ccw'
	
