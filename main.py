import interface
import number_of_symbols as nos
import Reading


if __name__ == '__main__':
    url = 'https://github.com/Vetcher/pagedownloader/blob/master/pkg/cleaner/cleaner.go'
    text = Reading.reading(url)
    dictionary = nos.numbers_of_symbols(text)
    histogram = interface.histogram_of_symbols(dictionary)
    print(histogram)
