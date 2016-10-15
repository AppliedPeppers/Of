import unittest
import interface


class MyTestCase(unittest.TestCase):
    def test_1(self):
        dictionary = {'a' : 1, 'b' : 1}
        test = interface.histogram_of_symbols(dictionary)
        ans = 'a : #########################\nb : #########################\n'
        self.assertEqual(ans, test)

    def test_2(self):
        dictionary = {'a' : 1, 'b' : 4}
        test = interface.histogram_of_symbols(dictionary)
        ans = 'a : ##########\nb : ########################################\n'
        self.assertEqual(ans, test)


if __name__ == '__main__':
    unittest.main()
