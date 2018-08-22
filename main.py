import sys
from lexer import lex
from parser import parse

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
		f=open(source_file, "r")

		if f.mode == 'r':
			contents =f.read()
			#contents = contents.replace('\n','')
			token_list = lex(contents)

			if len(sys.argv) > 2:
				print "Token List: " , token_list
			
			parse(token_list)

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











