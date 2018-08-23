from ASTNodes import Program, Function, Return, Constant, UnOp

op_list = []

'''
Creates assembly.s
'''
def create(ast):
	file = open("assembly.s", "w") 
	parseTree(ast, file)

'''
Traverses the syntax tree and generates assembly to assembly.s
'''
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
			if isinstance(curr.next(), Constant):
				ret_val = curr.getExpression().getValue()
				file.write("\tmovl $" + ret_val + ", %eax\n\tret\n")
			
			curr = curr.next()

		elif isinstance(curr, Constant):
			curr = curr.next()

		elif isinstance(curr, UnOp):
			if isinstance(curr.getExpression(), Constant):
				op_list.append(curr.getOperator())
				ret_val = curr.getExpression().getValue()
				file.write("\tmovl $" + ret_val + ", %eax\n")
				while len(op_list) != 0:
					op = op_list.pop()
					if op == "-":
						file.write("\tneg %eax\n")
					elif op == "~":
						file.write("\tnot %eax\n")
				file.write("\tret\n")
			elif isinstance(curr.getExpression(), UnOp):
				op_list.append(curr.getOperator())
			curr = curr.next()

	file.close()

