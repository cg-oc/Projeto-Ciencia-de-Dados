import sys
import unittest
from unittest.mock import patch
# Substitua 'main' pela função do vias.py que executa a lógica principal
from vias import main 

class TestViasAutomatizado(unittest.TestCase):

    @patch('builtins.input')
    def test_execucao_com_dados_fornecidos(self, mock_input):
        # Lista com todos os inputs que o programa espera receber, em ordem
        longo = [
            "13 14 3",
            "2 9 2",
            "4 2 1",
            "7 8 2",
            "4 5 1",
            "1 3 1",
            "5 3 2",
            "9 4 2",
            "7 2 2",
            "6 1 1",
            "5 9 1",
            "5 6 2",
            "10 6 1",
            "11 12 1",
            "11 13 1"
        ]
        medio = [
            "3 6 0",
            "1 2 1",
            "2 1 1",
            "1 3 1",
            "3 1 1",
            "2 3 1",
            "3 2 1"
        ]
        curto = [
            "2 2 2",
            "1 2 1",
            "1 3 1"
        ]
        TIPO_INPUT = curto
        
        # Define o comportamento do mock_input para retornar cada item da lista sequencialmente
        mock_input.side_effect = TIPO_INPUT

        # Executa a função principal do seu programa
        # Se o programa esperar exatamente 15 inputs, ele vai consumir a lista acima
        try:
            main()
        except Exception as e:
            self.fail(f"O programa falhou durante a execução com os inputs fornecidos: {e}")

        # Opcional: Validar se o mock_input foi chamado o número correto de vezes
        self.assertEqual(mock_input.call_count, len(TIPO_INPUT))

if __name__ == '__main__':
    unittest.main()