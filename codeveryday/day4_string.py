

# how string works in python
# three ways to generate a string
s1='hello'
s2="hello world!"
s3='''
hello,
this ugly and amazing
world!
'''
print(s1,s2,s3)

# different encoding,o,x0,unicode

s4 = '\141\142\143\x61\x62\x63'
s5 = '\u9a86\u660a'
print(s4, s5)

# operation cat, in not in,slice[start:stop:step]

scat=s4+s5

print(scat)
print('he' in s1)
print(s1[:4])