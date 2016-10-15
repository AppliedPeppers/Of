
num_of_rangs = 50


def high_of_column(n):
    s = ''
    for i in range(n):
        s += '#'
    return s


def histogram_of_symbols(dic):
    ret_string = ''
    l = sum([val for key, val in dic.items()])
    for key, value in dic.items():
        percents_of_syms = value / l
        num_of_cols = round(percents_of_syms * num_of_rangs)
        ret_string += '{symbol} : {column}\n'.format(symbol=key,
                                                     column=high_of_column(num_of_cols))
    return ret_string
