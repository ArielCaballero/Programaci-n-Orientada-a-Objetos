import unittest

import Palindromo

class TestPalindromos(unittest.TestCase):
    def setUp(self):
        self.__palindromo=Palindromo.Palindromo("")
    def testvacio(self):
        self.__palindromo.setPalabra("")
        self.assertFalse(self.__palindromo.nuevoesPalindromo())
    def testpalindromopar(self):
        self.__palindromo.setPalabra("alla")
        self.assertTrue(self.__palindromo.nuevoesPalindromo)
    def testpalindromoimpar(self):
        self.__palindromo.setPalabra("neuquen")
        self.assertTrue(self.__palindromo.nuevoesPalindromo)
    def testNopalindromopar(self):
        self.__palindromo.setPalabra("papa")
        self.assertFalse(self.__palindromo.nuevoesPalindromo())
    def testNopalindromoimpar(self):
        self.__palindromo.setPalabra("capaz")
        self.assertFalse(self.__palindromo.nuevoesPalindromo())


if __name__=="__main__":
    unittest.main()