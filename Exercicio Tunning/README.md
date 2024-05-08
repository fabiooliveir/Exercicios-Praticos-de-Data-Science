# Treinamento e Teste de Modelos de Empréstimo Pessoal

Este projeto tem como objetivo treinar e testar modelos de machine learning para prever a probabilidade de um cliente solicitar um empréstimo pessoal.

## Dados

Os dados utilizados neste projeto estão no arquivo `Bank_Personal_Loan_Modelling.xlsx` e incluem as seguintes colunas:

- `Age`: Idade do cliente
- `Experience`: Anos de experiência profissional
- `Income`: Renda anual do cliente
- `Family`: Tamanho da família do cliente
- `CCAvg`: Gasto médio em cartão de crédito por mês
- `Education`: Nível de educação do cliente (1: bacharelado, 2: mestrado, 3: doutorado)
- `Mortgage`: Valor do empréstimo hipotecário restante
- `CreditCard`: Se o cliente possui cartão de crédito (1: sim, 0: não)
- `Securities_Account`: Se o cliente possui conta de valores mobiliários (1: sim, 0: não)
- `CD_Account`: Se o cliente possui certificado de depósito (1: sim, 0: não)
- `Online`: Se o cliente usa serviços bancários online (1: sim, 0: não)
- `Personal_Loan`: Se o cliente aceitou o empréstimo pessoal anteriormente (1: sim, 0: não)

## Pré-requisitos

Para executar este projeto, é necessário ter instalado o Python (preferencialmente versão 3) e as seguintes bibliotecas:

- pandas
- scikit-learn

Você pode instalar as bibliotecas necessárias executando o seguinte comando:

```bash
pip install pandas scikit-learn
