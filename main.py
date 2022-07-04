import re

r = "(hi|hello|hey)[ ]*([a-z]*)"

print(re.match(r, 'Hello Rosa', flags=re.IGNORECASE))
print(re.match(r, 'hi ho hi ho hi ho', flags=re.IGNORECASE))
print(re.match(r, 'hey, dude', flags=re.IGNORECASE))

r = "[^a-z]*([y]o|[h']?ello|ok|hey|(good[ ])?(morn[gin']{0,3}|afternoon|even[gin']{0,3}))[ ,;:]{1,3}([a-z]{1,20})"

re_greeting = re.compile(r, flags=re.IGNORECASE)
print(re.match(r, "Hello friend", flags=re.IGNORECASE))
print(re.match(r, "ok Rosa", flags=re.IGNORECASE))
print(re.match(r, "mornin' dear", flags=re.IGNORECASE))
