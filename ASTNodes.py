class Constant():
	
	value = 0
	
	# The class "constructor" - It's actually an initializer 
	def __init__(self, value):
		self.value = value

	def getValue(self):
		return self.value

class Return():

	value = 0

	def __init__(self, value):
		self.value = value

	def getValue(self):
		return self.value

class Function():

	string = ""
	statement = 0

	def __init__(self, string, statement):
		self.string = string
		self.statement = statement
	
	def getString(self):
		return self.string

	def getStatement(self):
		return self.statement

def Program():

	function_declaration = 0

	def __init__(self, func):
		self.function_declaration = func

	def getFunction(self):
		return self.function_declaration

