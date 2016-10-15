def numbers_of_symbols(text):
    dictionary = {}
    i = 0
    while i < len(text):
        if dictionary.get(text[i]) is None:
            dictionary.setdefault(text[i], 1)
        else:
            other = [text[i], dictionary.get(text[i]) + 1]
            dictionary.update(other)
        i += 1
    return dictionary
