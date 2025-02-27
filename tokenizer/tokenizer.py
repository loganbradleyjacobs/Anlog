from .tokenizer_functions import code_cleaner, split_by_delimiters

def tokenize(source_filepath, delimiters):
   """
   Tokenize the source code from the given filepath.
   """
   all_tokens = []
   with open(source_filepath, 'r') as source_file:
      for code_line in source_file:
         code_line = code_cleaner(code_line)
         tokens = split_by_delimiters(code_line, delimiters)
         if tokens:
            all_tokens.extend(tokens)
   return all_tokens
