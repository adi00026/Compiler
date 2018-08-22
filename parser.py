import sys

'''
Recursive descent parser. Each method corresponds to a nonterminal symbol in the grammar.
Parses a stream of tokens using LR(1). Returns error messages.
'''
def parse(token_list):
	parse_program(iter(token_list))

def parse_program(tokens):
	parse_function_declaration(tokens)
	
def parse_function_declaration(tokens):
	tok = tokens.next()
	if tok[0] != "Type":
		fail("Missing return type.")
	tok = tokens.next()
	if tok[0] != "Identifier":
		fail("Missing identifer.")
	tok = tokens.next()
	if tok[0] != "Open-Paren":
		fail("Missing (")
	tok = tokens.next()
	if tok[0] != "Close-Paren":
		fail("Missing )")
	tok = tokens.next()
	if tok[0] != "Open-Brace":
		fail("Missing {")
	parse_statement(tokens)

def parse_statement(tokens):
    tok = tokens.next()
    if tok[0] != "Keyword":
        fail("Missing keyword")

    parse_expression(tokens)
   
    tok = tokens.next()
    if tok[0] != "Semicolon":
        fail("Missing ;")

def parse_expression(tokens):
	tok = tokens.next()
	if tok[0] != "Integer":
		fail("Missing integer.")

def fail(err):
	print "ERROR " + err
	sys.exit()