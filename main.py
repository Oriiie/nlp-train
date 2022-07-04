import re
r = "(hi|hello|hey)[ ]*([a-z]*)"

print(re.match(r, 'Hello Rosa', flags=re.IGNORECASE))
print(re.match(r, 'hi ho hi ho hi ho', flags=re.IGNORECASE))
print(re.match(r, 'hey, dude', flags=re.IGNORECASE))
