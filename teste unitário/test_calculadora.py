import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_positivo_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)
    
    def test_soma_varias_entradas(self):
        x_y_saidas = ((
            (10, 20, 30),
            (-10, 10, 0),
            (0, 0, 0),
            (1.5, 2.5, 4.0),
            (-1.5, -2.5, -4.0),
        ))
        for x, y, saida_esperada in x_y_saidas:
            with self.subTest(x=x, y=y, saida_esperada=saida_esperada):
                self.assertEqual(soma(x, y), saida_esperada)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('10', 5)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(5, '10')

unittest.main(verbosity=2)  # Executa os testes quando o arquivo é executado diretamente