class SimpleTest():
	prefix = 'Said: '
	postfix = '\n' + '-'*10

	def myprint(self, string):
		print(self.prefix + string + self.postfix)

simple1 = SimpleTest()
simple1.myprint('harati')