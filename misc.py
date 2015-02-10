def euclide(a,b):
	r0 = max(a,b)
	r1 = min(a,b)
	xn,xn1 = 0,1
	yn,yn1 = 1,0

	if r1 == 0:
		return r0, 0, 1

	while r0%r1 != 0:
		xn,xn1 = xn1-(r0//r1)*xn,xn
		yn,yn1 = yn1-(r0//r1)*yn,yn
		r0,r1 = r1, r0%r1 

	return r1,xn,yn
