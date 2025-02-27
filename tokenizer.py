import tokenizer_functions as tokenizer_functions


source_filepath = "int_prototype.anlog"
split_operators = [" ","\n"]

with open(source_filepath, 'r') as source_file:
   for code_line in source_file:
      tokenizer_functions.code_cleaner(code_line)

