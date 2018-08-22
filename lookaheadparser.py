import sys

'''
Recursive descent parser. Each method corresponds to a nonterminal symbol in the grammar.
Parses a stream of tokens using LR(1). Returns error messages.
'''
token_list = []

def parse(tokens):
	global token_list
	token_list = tokens
	parse_program()

def parse_program():
	parse_function_declaration()
	
def parse_function_declaration():
	tok = nextToken()
	if tok[0] != "Type":
		fail("Missing return type.")
	tok = nextToken()
	if tok[0] != "Identifier":
		fail("Missing identifer.")
	tok = nextToken()
	if tok[0] != "Open-Paren":
		fail("Missing (")
	tok = nextToken()
	if tok[0] != "Close-Paren":
		fail("Missing )")
	tok = nextToken()
	if tok[0] != "Open-Brace":
		fail("Missing {")
	parse_statement()

def parse_statement():
    tok = nextToken()
    if tok[0] != "Keyword":
        fail("Missing keyword")
    parse_expression()
    tok = nextToken()
    if tok[0] != "Semicolon":
        fail("Missing ;")

def parse_expression():
	tok = nextToken()
	if tok[0] != "Integer":
		fail("Missing integer.")

def fail(err):
	print "ERROR " + err
	sys.exit()

def nextToken():
	global token_list
	a = token_list[0]
	token_list = token_list[1:]
	return a

