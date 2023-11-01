import re

pattern = '^b..a$'
test_string = 'baba'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	
