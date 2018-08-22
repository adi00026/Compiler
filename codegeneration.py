from ASTNodes import Program, Function, Return, Constant

'''
Generates x86 assembly.
'''
def create(ast):
	file = open("assembly.s", "w") 
	parseTree(ast, file)

def parseTree(ast, file):

	curr = ast

	while curr:
		
		if isinstance(curr, Program):
			curr = curr.getFunction()

		elif isinstance(curr, Function):
			func_name = curr.getName()
			file.write(".globl _" + func_name + "\n _" + func_name + ":\n")
			curr = curr.getStatement()
		
		elif isinstance(curr, Return):
			ret_val = curr.getExpression().getValue()
			file.write("\tmovl $" + ret_val + ", %eax\n\tret")
			curr = curr.getExpression()

		elif isinstance(curr, Constant):
			curr = curr.next()

	file.close()

