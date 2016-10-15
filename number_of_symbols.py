

"""def numbers_of_symbols(str):

    dictionary = {'syms': 0 ,'number': 0}
    i = 0
    while(1):
        if (str[i])


    return number"""

d = {'syms': 0, 'numb': 0}

str = 'abcaaaa'
i = 0
num = 0
other = ['a', 1]
print(len(str))
while (i < len(str)):
    if (str[i] == 'a'):
        num = num + 1
        other[1] = num
    i = i + 1

d.update([other])
print(d.keys())
print(d.get('a'))
