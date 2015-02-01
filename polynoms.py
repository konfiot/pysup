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
		return Polynom([self[x]+other[x] for x in range(max(self.deg()-1, other.deg()-1))])
	
	def __iadd__(self, other):
		while self.deg() < other.deg():
			self.coefs.append(0)
		for x in range(self.deg()-1):
			self[x] += other[x]
		return self

	def __getitem__(self, i):
		if i > self.deg() : return 0
		else : return self.coefs[i]

	def deg(self):
		return len(self.coefs)-1 # TODO : Eliminer les coefficients nuls

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
		for i in range(self.deg()+1):
			out += str(self[i]) + "X^"+str(i) + " + "
		return out
