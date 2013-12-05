import re
"""
# Your code goes here
find = []
dir = dir(re)
for i in dir:
  if dir.find("find"):
  	find.append(i)
print find.sort() 
"""

find = []
for i in dir(re):
	if "find" in i:
		find.append(i)

print (sorted(find))

