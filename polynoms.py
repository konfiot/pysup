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
		return Polynom([self[x]+other[x] for x in range(max(self.deg(), other.deg())+1)])
	
	def __iadd__(self, other):
		while self.deg() < other.deg():
			self.coefs.append(0)
		for x in range(self.deg()):
			self[x] += other[x]
		return self

	def __getitem__(self, i):
		if i > len(self.coefs)-1 : return 0
		else : return self.coefs[i]

	def deg(self):
		if self.coefs == [0]*len(self.coefs):
			return -1

		while self.coefs[-1] == 0:
			del self.coefs[-1]
		return len(self.coefs)-1

	def __mul__(self,other):
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
		out = ""
		for i in range(len(self.coefs)):
			out += str(self[i]) + "X^"+str(i) + " + "
		return out[0:-3]

	def __eq__(self, other):
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
			for i in range(p-1):
				P *= self
		return P

	@staticmethod
	def division(A,B):
		if B.deg() > A.deg():
			return (Polynom([0]),A)
		else :
			C = Polynom([A[A.deg()]/B[B.deg()]])*(Polynom([0,1])**(A.deg()-B.deg()))
			Q,R = Polynom.division(A+(-(C*B)), B)
		return Q+C,R


	def __floordiv__(A,B):
		Q,R = Polynom.division(A,B)
		return Q

	def __mod__(A,B):
		Q,R = Polynom.division(A,B)
		return R

