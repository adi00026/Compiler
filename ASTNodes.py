class Constant():
	
	value = 0
	
	def __init__(self, value):
		self.value = value

	def getValue(self):
		return self.value

	def next(self):
		return False

class Return():

	expression = ""

	def __init__(self, expression):
		self.expression = expression

	def getExpression(self):
		return self.expression

	def next(self):
		return self.expression

class Function():

	name = ""
	statement = 0

	def __init__(self, name, statement):
		self.name = name
		self.statement = statement
	
	def getName(self):
		return self.name

	def getStatement(self):
		return self.statement

class Program():

	function_declaration = 0

	def __init__(self, func):
		self.function_declaration = func

	def getFunction(self):
		return self.function_declaration

	def getNext(self):
		return self.function_declaration

class UnOp():

	oper = ""
	inner_exp = ""

	def __init__(self, oper, inner_exp):
		self.oper = oper
		self.inner_exp = inner_exp

	def getExpression(self):
		return self.inner_exp

	def getOperator(self):
		return self.oper

	def next(self):
		if isinstance(self.inner_exp, UnOp):
			return self.inner_exp
		else:
			return False
