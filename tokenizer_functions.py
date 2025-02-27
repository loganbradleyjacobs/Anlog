def remove_comments(code_line):
   if code_line[:2] == "//":
      return ""
   else:
      return code_line

def code_cleaner(code_line):
   code_line = remove_comments(code_line)
   if code_line != "":
      code_line = code_line.strip()
      print(code_line, end = "")
