from misc import euclide

class MFraction():
	def __init__(self, num, den):
		if isinstance(num, MFraction) or isinstance(den, MFraction):
			frac = num/den
			self.num = frac.num
			self.den = frac.den
		else :
			self.num = num
			self.den = den

		p, x, y = euclide(self.num, self.den)
		self.den //= p
		self.num //= p

	def __add__(A,B):
		if not isinstance(B, MFraction):
			return MFraction(A.num + A.den*B,A.den)
		return MFraction(A.num*B.den + A.den*B.num,A.den*B.den)
	
	def __radd__(A,B):
		return A + B

	def __rmul__(A,B):
		return A*B

	def __mul__(A,B):
		if not isinstance(B, MFraction):
			return MFraction(A.num*B,A.den)
		return MFraction(A.num*B.num,A.den*B.den)

	def __sub__(A,B):
		if not isinstance(B, MFraction):
			return MFraction(A.num - A.den*B,A.den)
		return MFraction(A.num*B.den - A.den*B.num,A.den*B.den)

	def __rdiv__(A,B):
		return A/B

	def __rtruediv__(A,B):
		return A/B

	def __div__(A,B):
		if not isinstance(B, MFraction):
			return MFraction(A.num,A.den*B)
		return MFraction(A.num*B.den,A.den*B.num)

	def __truediv__(A,B):
		if not isinstance(B, MFraction):
			return MFraction(A.num,A.den*B)
		return MFraction(A.num*B.den,A.den*B.num)

	def __eq__(A,B):
		if not isinstance(B, MFraction):
			return A.num == B*A.den
		return A.num*B.den == A.den*B.num

	def __lt__(A,B):
		diff = A-B
		return (diff.num > 0)^(diff.den > 0)

	def __gt__(A,B):
		return not A < B

	def __neg__(self):
		return MFraction(-self.num, self.den)

	def __str__(self):
		A = str(self.num)
		B = str(self.den)
		m = max(len(A), len(B))
		A += "\n" + "-"*m + "\n"
		A += B + "\n"
		return A

	def reduce(self):
		(pgcd, x, y) = euclide(self.num, self.den)
		print(pgcd)
		return MFraction(self.num // pgcd, self.den // pgcd)

	def ent(self):
		return self.num//self.den

	def frac(self):
		return self.num%self.den
