<div align="center">
  <img src="imagens/cabecalho_branco.jpg" alt="Cabeçalho do Projeto" width="100%">
</div>

# Arquipélago e Vias

O **Arquipélago e Vias** é um programa em Python para modelar um arquipélago como um grafo, no qual ilhas são vértices e vias são arestas. O programa diferencia rodovias rompíveis e hidrovias permanentes, visualiza a evolução do grafo e verifica se a configuração do arquipélago permanece simples ou apresenta ciclos excessivos.

## 📸 Demo

https://github.com/user-attachments/assets/957c8589-ccaf-4e79-b4db-7a86fe0ad8aa


## 📦 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/cg-oc/Projeto-Ciencia-de-Dados.git
cd Projeto-Ciencia-de-Dados
pip install -r requirements.txt
```

## Lógica e temática

O arquivo ```juvias.ipynb``` explica o algoritmo desenvolvido a partir de seções do código, como a classe `Arquipelago`, seus métodos e a lógica utilizada.
A temática dessa abordagem, baseada em ilhas de um arquipélago ligadas por rodovias e hidrovias, é inspirada em uma questão elaborada pela Olimpíada Brasileira
de Informática [1].

## 🛠 Uso

Rode o programa:

```bash
python vias.py
```

Ou rode o **Jupyter Notebook** ```juvias.ipynb```.


## Entrada

A entrada inicial contém dois inteiros:

- `C`: número de conexões a serem cadastradas;
- `A`: número de anos do período de análise.

Em seguida, são informadas `C` conexões, cada uma contendo:

- o nome do primeiro vértice;
- o nome do segundo vértice;
- o tipo de via:
  - `r`: rodovia, considerada rompível;
  - `h`: hidrovia, considerada permanente.
  

## Saída
- Atualização de uma imagem `.png` para visualizar o grafo a cada etapa da análise;
- Após todas as análises, imprime no terminal se o arquipélago era simples ou não.


Exemplo de entrada/saída:
- OBS: O prompt `ENTER para continuar` pausa a execução do programa e espera pelo usuário para atualizar a imagem `.png` do grafo.
  
```bash
$ python vias.py
Número de conexões, anos: 3 0 
USO: <vértice 1> (texto) <vértice 2> (texto) <tipo de via> (r ou h) --- Ex: hospital mercado r
vértice 1, vértice 2, tipo de via: casa faculdade r  
vértice 1, vértice 2, tipo de via: faculdade mercado r
vértice 1, vértice 2, tipo de via: mercado casa h
ENTER para continuar
ENTER para continuar
ENTER para continuar
ENTER para continuar
O arquipélago não era simples!
```
Última visualização gerada:

<img loading="lazy" src="imagens/meu_grafo.jpg" width=450> 


## ✨ Funcionalidades

- Detecção de ciclos excessivos em grafos;
- Distinção entre conexões rompíveis e permanentes;
- Configuração de limites de conexões rompíveis para parada do programa;
- Visualização da evolução do grafo.

## 🐍 Versão do Python e módulos

- Python: 3.13.7
- matplotlib: 3.11.0
- networkx: 3.6.1

## 📄 Licença

GNU General Public License v3.0

Leia o arquivo `LICENSE` para mais detalhes.

## 📖 Referência

1. Inspirado pela questão-problema [Hidrovias e Rodovias](https://olimpiada.ic.unicamp.br/static/extras/obi2025/provas/ProvaOBI2025_f3ps.pdf) de uma prova da Olimpíada Brasileira de Informática.

## Desenvolvedor do Projeto

| [<img loading="lazy" src="imagens/fotopessoal.jpg" width=145><br><sub>Carlos Gabriel de Oliveira Campos</sub>](https://github.com/cg-oc) |
| :---: |
Aluno do primeiro semestre de Ciência e Tecnologia, na Ilum Escola de Ciência

## 🎓 Professores

**Prof. Dr. Daniel Roberto Cassar**
- **Contato:** `daniel.cassar@ilum.cnpem.br`
---
**Prof. Dr. James Moraes de Almeida**
- **Contato:** `james.almeida@ilum.cnpem.br`
---
**Prof. Dr. Leandro Nascimento Lemos**
- **Contato:** `leandro.lemos@ilum.cnpem.br`
---


 A eles, todos os meus agradecimentos por enriquecerem minhas habilidades e meu raciocínio!

<div align="center">
  <img src="imagens/rodape.jpg" alt="Cabeçalho do Projeto" width="100%">
</div>
