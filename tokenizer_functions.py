import re

def remove_comments(code_line):
   if code_line[:2] == "//":
      return ""
   else:
      return code_line

def code_cleaner(code_line):
   code_line = remove_comments(code_line)
   code_line = code_line.strip()
   if code_line == "":
      return code_line
   else:
      return code_line + "\n"
   
def split_by_delimiters(text, delimiters):
   tokenized_line = re.split(r'[ \n()]',text)
   if tokenized_line != ['']:
      return tokenized_line
   else:
      return None
   
