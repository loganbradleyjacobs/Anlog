from tokenizer.tokenizer import tokenize
#from lexer.lexer import lex

source_filepath = "int_prototype.anlog"
delimiters = " \n()"

tokens = tokenize(source_filepath, delimiters)
print(tokens)