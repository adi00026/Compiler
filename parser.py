import ASTNodes
import sys

'''
Parses a stream of tokens.
'''
def parse(token_list):
	tokens = iter(token_list)
	parse_program(tokens)
	#return parse_program(tokens)


def parse_program(tokens):
	
	parse_function_declaration(tokens)
	#return program


def parse_function_declaration(tokens):
	tok = tokens.next()
	if tok[0] != "Type":
		fail()
	tok = tokens.next()
	if tok[0] != "Identifier":
		fail()
	tok = tokens.next()
	if tok[0] != "Open-Paren":
		fail()
	tok = tokens.next()
	if tok[0] != "Close-Paren":
		fail()
	tok = tokens.next()
	if tok[0] != "Open-Brace":
		fail()

	print list(tokens)

	#return function_declaration 




# def parse_statement(tokens):
#     tok = tokens.next()
#     if tok.type != "RETURN_KEYWORD":
#         fail()
#     tok = tokens.next()
#     if tok.type != "INT"
#         fail()
#     exp = parse_exp(tokens) //parse_exp will pop off more tokens
#     statement = ASTNodes.Return(exp)

#     tok = tokens.next()
#     if tok.type != "SEMICOLON":
#         fail()

#     return statement
	

# def parse_expression(tokens):

# 	return constant

def fail():
	print "ERROR"
	sys.exit()