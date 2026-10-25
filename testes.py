import unittest;
import numeroromano as nr;
from numeroromano import converte;

class TestConversorRomanos(unittest.TestCase):

    def setUp(self):
        print('Teste', self._testMethodName, 'sendo executado...');

    def teste_valores(self):
        self.assertEqual(1, converte("I"), 'Valores incoerentes');
        self.assertEqual(5, converte("V"), 'Valores incoerentes');
        self.assertEqual(2, converte("II"), 'Valores incoerentes');
        self.assertEqual(22, converte("XXII"), 'Valores incoerentes');
        self.assertEqual(9, converte("IX"), 'Valores incoerentes');
        self.assertEqual(24, converte("XXIV"), 'Valores incoerentes');

    def tearDown(self):
        print('Teste', self._testMethodName, 'finalizado.'); 

if __name__ == "__main__":
    unittest.main()