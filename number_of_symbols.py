def numbers_of_symbols(str):
    dictionary = {}
    i = 0
    while (i < len(str)):
        if (dictionary.get(str[i])) == None:
            dictionary.setdefault(str[i], 1)
        else:
            other = [str[i], dictionary.get(str[i]) + 1]
            dictionary.update([other])
        i = i + 1
    return dictionary