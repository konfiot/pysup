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
		return Polynom([self[x]+other[x] for x in range(max(self.deg(), other.deg()))])
	
	def __iadd__(self, other):
		while self.deg() < other.deg():
			self.coefs.append(0)
		for x in range(self.deg()):
			self[x] += other[x]
		return self

	def __getitem__(self, i):
		if i > self.deg() : return 0
		else : return self.coefs[i]

	def deg(self):
		count = -1
		for i in self:
			if i == 0:
				return count
			count += 1

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

	def __eq__(self, other):
		if self.deg() == other.deg():
			for i in range(self.deg()):
				if self[i] != other[i]:
					return False
			return True
		else : return False
	def __neg__(self):
		coefs = [0]**self.deg()
		for i in range(self.deg()):
			coefs[i] = -self.coefs[i]
		return Polynom(coefs)
