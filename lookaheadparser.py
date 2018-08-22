import sys
from ASTNodes import Program, Function, Return, Constant

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
	if tok[0] != "Integer":
		fail("Missing integer.")
	return Constant(tok[1])

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

