class Fraction():
	def __init__(self, num, den):
		self.num = num
		self.den = den

	def __add__(A,B):
		return Fraction(A.num*B.den + A.den+B.num,A.den*B.den)

	def __mul__(A,B):
		return Fraction(A.num*B.num,A.den*B.den)

	def __sub__(A,B):
		return Fraction(A.num*B.den - A.den+B.num,A.den*B.den)

	def __div__(A,B):
		return Fraction(A.num*B.den,A.den*B.num)

	def __eq__(A,B):
		return A.num*B.den == A.den*B.num

	def __lt__(A,B):
		diff = A-B
		return (diff.num > 0)^(diff.den > 0)

	def __gt__(A,B):
		return not A < B

