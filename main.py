import sys
from lexer import lex
import parser
import lookaheadparser
from codegeneration import create

'''
Rules For Identifiers:
	They must begin with a letter or underscore(_).
	They must consist of only letters, digits, or underscore. No other special character is allowed.
	It should not be a keyword.
	It must not contain white space.
	It should be up to 31 characters long as only first 31 characters are significant.
'''

'''
Accepts C program from user, reads it and passes it to lexer for lexical analysis.
'''
def main():
	source_file = sys.argv[1]
	if check_file(source_file):
		
		f = open(source_file, "r")
		
		if f.mode == 'r':
			contents = f.read()
			compile(contents)

'''
Produces a token list by calling the lexer and uses the token list to produce an abstract syntax tree.
'''
def compile(contents):
	token_list = lex(contents)			
	#print "Token List: " , token_list
	ast = lookaheadparser.parse(token_list)
	create(ast)
	#print "Created ast"

'''
Checks if .c file is passed to the compiler. 
'''
def check_file(source_file):
	if not source_file.rstrip().endswith('.c'):
		print "ERR: not a valid .c file"
		return False
	return True

if __name__=='__main__':
	main()











