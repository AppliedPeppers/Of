
num_of_rangs = 50


def high_of_column(n):
    s = ''
    for i in range(n):
        s += '#'
    return s


def histogram_of_symbols(dic):
    ret_string = ''
    l = len(dic)
    percents_of_syms = [val / l for key, val in dic.items()]
    for key, value in dic.items():
        ret_string += '{symbol} : {column}'.format(symbol=key,
                                                   column=high_of_column(round(percents_of_syms * num_of_rangs)))
    return ret_string
