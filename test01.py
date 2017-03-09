# coding = utf-8 
class Programmer(object):
	"""docstring for ClassName"""
	def __init__(self, name,age,):
		self._age= age
		self.name = name
	def function(self):
		print"%s is %s"%(self.name,self._age)


class BrokenProgrammer(Programmer):
	"""docstring for ClassName"""
	def __init__(self, name,age):
		super(BrokenProgrammer, self).__init__(name)
		self.arg = arg
		self._name = name

if __name__ == '__main__':
	programmer = Programmer('xingxing',18)
	programmer.function()


		