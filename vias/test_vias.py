import sys
import unittest
from unittest.mock import patch
# Substitua 'main' pela função do vias.py que executa a lógica principal
from vias import main 

class TestViasAutomatizado(unittest.TestCase):
    # Variável de classe para armazenar o tipo escolhido (padrão é "curto")
    TIPO_ESCOLHIDO = "curto"

    @patch('builtins.input')
    def test_execucao_com_dados_fornecidos(self, mock_input):
        # Dicionário mapeando o nome do argumento para a lista correspondente
        cenarios = {
            "longo": [
                "13 14 0", "2 9 2", "4 2 1", "7 8 2", "4 5 1", 
                "1 3 1", "5 3 2", "9 4 2", "7 2 2", "6 1 1", 
                "5 9 1", "5 6 2", "10 6 1", "11 12 1", "11 13 1"
            ],
            "medio": [
                "3 6 0", "1 2 1", "2 1 1", "1 3 1", "3 1 1", "2 3 1", "3 2 1"
            ],
            "curto_loop": [
                "2 3 0", 
                "1 2 1", "1 3 1", "2 3 1"
            ],
            "curto": [
                "2 2 2", "1 2 1", "1 3 1"
            ]
        }
        
        # Busca o cenário escolhido. Se o usuário digitar algo inválido, usa o "curto" por padrão
        tipo_input = cenarios.get(self.TIPO_ESCOLHIDO, cenarios["curto"])
        
        # Define o comportamento do mock_input para retornar cada item da lista sequencialmente
        mock_input.side_effect = tipo_input

        # Executa a função principal do seu programa
        try:
            main()
        except Exception as e:
            self.fail(f"O programa falhou durante a execução com os inputs fornecidos: {e}")

        # Validar se o mock_input foi chamado o número correto de vezes
        self.assertEqual(mock_input.call_count, len(tipo_input))

if __name__ == '__main__':
    # Verifica se um argumento foi passado (além do nome do arquivo script.py)
    if len(sys.argv) > 1:
        # Guarda o argumento na classe de teste (ex: "longo", "medio", "curto")
        TestViasAutomatizado.TIPO_ESCOLHIDO = sys.argv[1].lower()
        
        # Removemos o argumento do sys.argv para o unittest não tentar interpretá-lo
        sys.argv = [sys.argv[0]]

    unittest.main()