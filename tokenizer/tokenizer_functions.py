import re

def remove_comments(code_line):
   """Transform commented lines to \"\"."""
   if code_line[:2] == "//":
      return ""
   else:
      return code_line

def code_cleaner(code_line):
   """Clean a line of code by handling comments and whitespace."""
   code_line = remove_comments(code_line)
   code_line = code_line.strip()
   if code_line == "":
      return code_line
   else:
      return code_line + "\n"
   
def split_by_delimiters(text, delimiters):
   """Split text into tokens based on delimiters"""
   pattern = f"[{re.escape(delimiters)}]"
   tokenized_line = re.split(pattern,text)
   
   filtered_tokens = [token for token in tokenized_line if token.strip()]
   return filtered_tokens if filtered_tokens else None
   
