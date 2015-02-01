class Polynom():
	self.coefs = []
	def __init__(self, coefs):
		self.coefs = coefs
	
	def __init__(self, maincoef, roots):
		sum = 0
		nfact = math.factorial(len(roots))
		for coef in range(len(roots)): # Pour chaque coefficient, on va calculer les relations coefficients racines
			for i in nfact//(math.factorial(coef)*math.factorial(len(roots)-coef)):
				
				
			

	def __add__(self, other):
		return Polynom([self[x]+other[x] for x in range(len(self.coefs))])

	def __getitem__(self, i):
		return self.coefs[i]

