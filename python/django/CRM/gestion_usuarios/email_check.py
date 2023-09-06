import re
 
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
 if(re.fullmatch(regex, email)):
  valid = True
 else:
  valid = False
 return valid