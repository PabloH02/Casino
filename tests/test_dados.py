import unittest
import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Dados 

class TestLanzarDados(unittest.TestCase):

    # Probar el lanzamiento de dados con valores controlados
    @patch('random.randint')
    def test_lanzar_dados(self, mock_randint):
        """Probar que la función lanzar_dados devuelve los valores esperados."""
        # Simulamos que el dado 1 devuelve 3 y el dado 2 devuelve 5
        mock_randint.side_effect = [3, 5]
        
        dado1, dado2 = Dados.lanzar_dados()
        
        # Verificamos que los valores devueltos sean los esperados
        self.assertEqual(dado1, 3)
        self.assertEqual(dado2, 5)
    
    # Probar el lanzamiento de dados con otros valores controlados
    @patch('random.randint')
    def test_lanzar_dados_otros_valores(self, mock_randint):
        """Probar que la función lanzar_dados devuelve correctamente otros valores."""
        # Simulamos que el dado 1 devuelve 1 y el dado 2 devuelve 6
        mock_randint.side_effect = [1, 6]
        
        dado1, dado2 = Dados.lanzar_dados()
        
        # Verificamos que los valores devueltos sean los esperados
        self.assertEqual(dado1, 1)
        self.assertEqual(dado2, 6)

if __name__ == '__main__':
    unittest.main()
