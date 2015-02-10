import misc
from fraction import MFraction

class Polynom():
	def __init__(self, coefs, maincoef = False):
		if maincoef :
			self.coefs=[maincoef]
			for root in coefs:
				print(root)
				self *= Polynom([-root,1])
				print(self)
		else : self.coefs = coefs

	def __add__(self, other):
		if not isinstance(other, Polynom):
			other = Polynom([other])
		return Polynom([self[x]+other[x] for x in range(max(self.deg(), other.deg())+1)])
	
	def __iadd__(self, other):
		if not isinstance(other, Polynom):
			other = Polynom([other])

		while self.deg() < other.deg():
			self.coefs.append(0)
		for x in range(self.deg()):
			self[x] += other[x]
		return self

	def __sub__(self, other):
		return self + (-other)

	def __radd__(self, other):
		return self+other

	def __rsub__(self, other):
		return self-other

	def __rmul__(self, other):
		return self*other

	def __getitem__(self, i):
		if i > len(self.coefs)-1 : return 0
		else : return self.coefs[i]

	def deg(self):
		if self.coefs == [0]*len(self.coefs):
			self.coefs = [0]
			return -1

		while self.coefs[-1] == 0:
			del self.coefs[-1]

		return len(self.coefs)-1

	def __mul__(self,other):
		if not isinstance(other, Polynom):
			other = Polynom([other])
		
		coefs = [0]*(self.deg() + other.deg()+1)
		for k in range(self.deg() + other.deg()+1):
			for i in range(k+1):
				coefs[k] += self[i]*other[k-i]
		return Polynom(coefs)

	def __imul__(self,other):
		coefs = [0]*(self.deg() + other.deg()+1)
		for k in range(self.deg() + other.deg()+1):
			for i in range(k+1):
				coefs[k] += self[i]*other[k-i]
		self.coefs = coefs	
		return self

	def __str__(self):
		up = ["⁰","¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹"]
		out = ""
		for i in range(len(self.coefs)):
			if self[i] == 0:
				continue

			exposant = ""
			x = i
			if i > 0 :
				if i > 1:
					while x > 0:
						exposant = up[x%10] + exposant
						x //= 10
				exposant = "x" + exposant
			out += str(self[i]) + exposant +  " + "

		return out[0:-3]

	def __eq__(self, other):
		if type(other) == int:
			return True if self.deg() <= 0 and self[0] == other else False

		if self.deg() == other.deg():
			for i in range(self.deg()):
				if self[i] != other[i]:
					return False
			return True
		else : return False

	def __neg__(self):
		coefs = [0]*(self.deg()+1)
		for i in range(self.deg()+1):
			coefs[i] = -self.coefs[i]
		return Polynom(coefs)
	
	def __pow__(self,p):
		P = Polynom(self.coefs)
		if p == 0:
			return Polynom([1])
		else :
			table = []
			while p > 0:
				if p%2:
					table.append(Polynom(P.coefs))
				p //= 2
				P *= P
		
		out  = 1
		for A in table :
			out *= A
		return out

	@staticmethod
	def division(A,B):
		if B.deg() > A.deg():
			return (Polynom([0]),A)
		else :
			C = Polynom([MFraction(A[A.deg()],B[B.deg()])])*(Polynom([0,1])**(A.deg()-B.deg()))
			Q,R = Polynom.division(A+(-(C*B)), B)
		return Q+C,R


	def __floordiv__(A,B):
		Q,R = Polynom.division(A,B)
		return Q

	def __mod__(A,B):
		Q,R = Polynom.division(A,B)
		return R
	
	def __gt__(A,B):
		return A.deg() > B.deg()

	def __lt__(A,B):
		return A.deg() < B.deg()

	def __xor__(A,B):
		P,X,Y = misc.euclide(A,B)
		return P*(MFraction(1,P[P.deg()]))

	def evaluate(self, t):
		out = 0
		for i,c in enumerate(self.coefs):
			out += (c**i)*t
		return out

	def ppcm(A,B):
		return A//((A^B)*A[A.deg()]*B[B.deg()])

	def diff(self, n):
		coefs = [coef for coef in self.coefs]
		for k in range(n):
			for i in range(len(coefs)-1):
				coefs[i] = coefs[i+1]*(i+1)
			coefs[-1] = 0
		return Polynom(coefs)

	def integrate(self, k):
		coefs = [coef for coef in self.coefs]
		coefs.append(0)
		for i in range(len(coefs)-1, 0, -1):
			coefs[i] = coefs[i-1]/i
		coefs[0] = k
		return Polynom(coefs)

X = Polynom([0,1])
