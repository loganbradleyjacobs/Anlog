import tokenizer_functions as tokenizer_functions


source_filepath = "int_prototype.anlog"
split_delimiters = " \n()"

with open(source_filepath, 'r') as source_file:
   for code_line in source_file:
      code_line = tokenizer_functions.code_cleaner(code_line)
      tokens = tokenizer_functions.split_by_delimiters(code_line, split_delimiters)
      if tokens != None:
         print(tokens)