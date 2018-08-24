keywords = ["auto", "struct", "break", "else", "switch", "case", "enum", "register", "typedef", "extern", "return", "union", "const", "unsigned", "continue", "for", "signed", "void" , "default", "goto", "sizeof", "volatile" , "do", "if", "static", "while"]
types = ["double", "int", "long", "char", "float", "short"] 

'''
Produces a stream of tokens.
Current terminals: Keyword, Identifier, Open-Paren, Closed-Paren, Open-Brace, Closed-Brace, Semicolon, Integer
'''
lineNumber = 1

def lex(source):	
	token_list = []
	x = 0
	newStr = ""
	global lineNumber
	while x < len(source):

		if source[x].isalpha() or source[x].isdigit() or source[x] == '_':
			newStr = newStr + source[x]

		elif source[x] == ' ': 
			token_list.append(check(newStr))
			newStr = ""

		elif source[x] == '\n':
			token_list.append(check(newStr))
			newStr = ""
			lineNumber = lineNumber + 1

		elif source[x] == "(":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Open-Paren", "(", lineNumber))
		
		elif source[x] == ")":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Close-Paren", ")", lineNumber))
		
		elif source[x] == "{":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Open-Brace", "{", lineNumber))

		elif source[x] == "}":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Close-Brace", "}", lineNumber))

		elif source[x] == ";":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Semicolon", ";", lineNumber))

		elif source[x] == "-":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Operator", "-", lineNumber))

		elif source[x] == "~":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Operator", "~", lineNumber))

		elif source[x] == "!":
			token_list.append(check(newStr))
			newStr = ""
			token_list.append(("Operator", "!", lineNumber))

		x = x + 1
	
	token_list = filter(None, token_list)
	return token_list

def check(newStr):
	if newStr == '' or newStr == '\n':
		return None
	elif newStr in keywords:
		return ("Keyword", newStr, lineNumber)
	elif newStr in types:
		return ("Type", newStr, lineNumber)
	elif newStr.isdigit():
		return ("Integer", newStr, lineNumber)
	elif len(newStr) > 0 and len(newStr) < 32:
		return ("Identifier", newStr, lineNumber)