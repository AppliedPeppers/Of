
num_of_rangs = 500

# возвращает строку с указанным кол-вом решеток(#)
def high_of_column(n):
    s = ''
    for i in range(n):
        s += '#'
    return s


# возвращает строку - гистограмму на основании словаря. кол-во решеток в гистограмме не более num_of_rangs
def histogram_of_symbols(dic):
    ret_string = ''
    l = sum([val for key, val in dic.items()])
    for key, value in dic.items():
        percents_of_syms = value / l  # частота появления символа
        num_of_cols = round(percents_of_syms * num_of_rangs)  # "высота" колонки
        ret_string += '{symbol}({per}%) : {column}\n'.format(symbol=key,
                                                             column=high_of_column(num_of_cols),
                                                             per=round(percents_of_syms, 5))
    return ret_string
