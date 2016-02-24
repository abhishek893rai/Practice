import re

stringEX ='''
Jessica is 15 years old, Daniel is 27 years old.
Edward is 97 and his grandfather,Oscar , is 102.
'''
print(stringEX)
ages = re.findall(r'\d{1,3}',stringEX)
names = re.findall(r'[A-Z][a-z]*',stringEX)

print(ages)
print(names)
print("\n")
dictCollect = {}
for i in range(len(ages)):
    dictCollect[names[i]]=ages[i]

print(dictCollect)
