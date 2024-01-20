
import unittest

from operaciones import sumar, restar, multiplicar, dividir


class TestSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(5, 8), 13)
        self.assertEqual(sumar(-3, 5), 2)
        self.assertEqual(sumar(-6, 2), -4)
         
class TestRestar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(restar(8, 3), 5)
        self.assertEqual(restar(3, 7), -4)
        self.assertEqual(restar(-2, -8), 6)

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 5), 20)
        self.assertEqual(multiplicar(0, 3), 0)
        self.assertEqual(multiplicar(3, 0), 0)
        self.assertEqual(multiplicar(-3, 2), -6)
        self.assertEqual(multiplicar(-5, -5), 25)
        
        
class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(10,5), 2)
        self.assertEqual(dividir(0,3), 0)
        self.assertEqual(dividir(3,0), None)# Validacion de la Division por 0
        

if __name__ == '__main__':
     unittest.main()