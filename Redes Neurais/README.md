# Projeto de Análise de Churn

Este projeto visa analisar a taxa de churn de uma empresa de acordo com diferentes variáveis, como tempo de contrato, método de pagamento, entre outros. O objetivo é criar modelos de Regressão Logística e Rede Neural para prever o churn dos clientes.

## Dataset

O dataset utilizado neste projeto é chamado 'churn.xlsx' e contém as seguintes colunas:

- customerID: ID do cliente
- tenure: Tempo de permanência em meses
- PhoneService: Serviço telefônico (Sim/Não)
- Contract: Tipo de contrato (Mensal, Anual, Bianual)
- PaperlessBilling: Faturamento sem papel (Sim/Não)
- PaymentMethod: Método de pagamento (Boleto, Cartão de Crédito, Transferência Bancária, Cheque Eletrônico)
- MonthlyCharges: Custo mensal
- TotalCharges: Custo total
- Churn: Variável target indicando se o cliente cancelou o serviço (Sim/Não)

## Pré-processamento dos dados

- As variáveis categóricas foram convertidas em variáveis dummy.
- O dataset foi dividido em conjunto de treino e teste (80% treino, 20% teste).

## Modelos

- Foi treinado um modelo de Regressão Logística para prever o churn dos clientes.
- Foi treinado um modelo de Rede Neural utilizando o módulo neural_network da biblioteca scikit-learn.

## Resultados

- A acurácia do modelo de Regressão Logística foi de X%.
- A acurácia do modelo de Rede Neural foi de Y%.

