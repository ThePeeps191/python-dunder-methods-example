class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f"Dog({self.name}, {self.age})"

	def __add__(self, item):
		if type(item) in [int, float]:
			return self.age + item

	def __sub__(self, item):
		if type(item) in [int, float]:
			return self.age - item

	def __mul__(self, item):
		if type(item) in [int, float]:
			return self.age * item

	def __div__(self, item):
		if type(item) in [int, float]:
			return self.age / item

bob = Dog("bob", 3)
print(bob)
print(bob + 2)
print(bob)
