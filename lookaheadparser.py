import sys
from ASTNodes import Program, Function, Return, Constant, UnOp
#import operator

'''
Recursive descent parser. Each method corresponds to a nonterminal symbol in the grammar.
Parses a stream of tokens using LR(1). Returns error messages.
'''
token_list = []

def parse(tokens):
	global token_list
	token_list = tokens
	return parse_program()

def parse_program():
	return Program(parse_function_declaration())
	
def parse_function_declaration():
	tok = nextToken()
	if tok[0] != "Type":
		fail("Missing return type.")
	tok = nextToken()
	if tok[0] != "Identifier":
		fail("Missing identifer.")
	func_name = tok[1]
	if len(func_name) > 32:
		fail("Identifier name too long.")
	tok = nextToken()
	if tok[0] != "Open-Paren":
		fail("Missing (")
	tok = nextToken()
	if tok[0] != "Close-Paren":
		fail("Missing )")
	tok = nextToken()
	if tok[0] != "Open-Brace":
		fail("Missing {")
	stmt = parse_statement()
	return Function(func_name, stmt)

def parse_statement():
    tok = nextToken()
    if tok[0] != "Keyword":
        fail("Missing keyword")
    exp = parse_expression()
    tok = nextToken()
    if tok[0] != "Semicolon":
        fail("Missing ;")
    return Return(exp)

def parse_expression():
	tok = nextToken()
	if tok[0] == "Integer":
		return Constant(tok[1])
	elif tok[0] == "Operator":
		inner_exp = parse_expression()
		return UnOp(tok[1], inner_exp)
	else:
		fail("Missing integer.")
	

def fail(err):
	print "ERROR " + err
	sys.exit()

def nextToken():
	global token_list
	a = token_list[0]
	token_list = token_list[1:]
	return a

def lookahead():
	global token_list
	return token_list[0]

# def get_operator(token):
# 	if tok[1] == '-':
# 		return operator.neg
# 	elif tok[1] == '~':
# 		return operator.invert
# 	elif tok[1] == '!':
# 		return operator.not_
