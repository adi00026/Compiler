keywords = ["auto", "struct", "break", "else", "switch", "case", "enum", "register", "typedef", "extern", "return", "union", "const", "unsigned", "continue", "for", "signed", "void" , "default", "goto", "sizeof", "volatile" , "do", "if", "static", "while"]
types = ["double", "int", "long", "char", "float", "short"] 

'''
Produces a stream of tokens.
Current terminals: Keyword, Identifier, Open-Paren, Closed-Paren, Open-Brace, Closed-Brace, Semicolon, Integer
'''
def lex(source):	
	token_list = []
	x = 0
	newStr = ""

	while x < len(source):

		if source[x].isalpha() or source[x].isdigit() or source[x] == '_':
			newStr = newStr + source[x]

		elif source[x] == ' ' or source[x] == '\n':
			token_list.append(check(newStr))			
			newStr = ""

		elif source[x] == "(":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Open-Paren", "("))
		
		elif source[x] == ")":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Close-Paren", ")"))
		
		elif source[x] == "{":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Open-Brace", "{"))

		elif source[x] == "}":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Close-Brace", "}"))

		elif source[x] == ";":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Semicolon", ";"))

		elif source[x] == "-":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Operator", "-"))

		elif source[x] == "~":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Operator", "~"))

		elif source[x] == "!":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Operator", "!"))

		x = x + 1
	
	token_list = filter(None, token_list)
	return token_list

def check(newStr):
	if newStr == '' or newStr == '\n':
		return None
	elif newStr in keywords:
		return ("Keyword", newStr)
	elif newStr in types:
		return ("Type", newStr)
	elif newStr.isdigit():
		return ("Integer", newStr)
	elif len(newStr) > 0 and len(newStr) < 32:
		return ("Identifier", newStr)