

"""def numbers_of_symbols(str):

    dictionary = {'syms': 0 ,'number': 0}
    i = 0
    while(1):
        if (str[i])


    return number"""

d = {}

str = 'abcaaaa'
i = 0
num = 0
other = ['a', 1]
#print(len(str))

while (i < len(str)):
    if (str[i] == 'a'):
        num = num + 1
        other[1] = num
    i = i + 1
print(d.keys())
d.update([other])
print(d.keys())
print(d.get('a'))\

d.setdefault(str[1])
print(d.keys())



