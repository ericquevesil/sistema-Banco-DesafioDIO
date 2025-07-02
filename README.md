Sistema Bancário em Python - Bootcamp DIO Santander 2025
Descrição do Projeto
Este projeto é um desafio do Bootcamp DIO Santander 2025 - Back-End com Python que consiste em implementar um sistema bancário simplificado em Python. O sistema permite três operações essenciais: depósito, saque e visualização de extrato, seguindo requisitos específicos para monetização das operações.

Funcionalidades
Operações disponíveis:
Depósito: Permite adicionar valores positivos à conta

Saque: Permite retirar dinheiro da conta (com limites e taxas)

Extrato: Exibe o histórico de transações e saldo atual

Regras de negócio:
Limite de saques: Máximo de 3 saques diários

Limite por saque: Valor máximo de R$ 500,00 por saque

Taxa por saque: Cobrança de R$ 1,50 por operação de saque

Formato do extrato: Lista todas as transações com data/hora, valores e taxas aplicadas

Pré-requisitos
Python 3.x instalado

Nenhuma dependência externa necessária

Como executar
Clone o repositório ou copie o código para um arquivo desafio.py

Execute o programa com o comando:

bash
python desafio.py
Siga as instruções no menu interativo

Estrutura do Código
O programa consiste em um loop principal que apresenta um menu com as seguintes opções:

text
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Exemplo de Uso
Ao iniciar o programa, você verá o menu principal

Digite 'd' para depósito e informe o valor desejado

Digite 's' para saque (lembrando dos limites e taxas)

Digite 'e' para visualizar seu extrato completo

Digite 'q' para sair do sistema

Melhorias Implementadas
Tratamento robusto de erros de entrada

Sistema de taxas para monetização

Extrato detalhado com data/hora das transações

Formatação profissional dos valores monetários

Feedback claro para o usuário em cada operação

Contribuição
Este projeto foi desenvolvido como parte do Bootcamp DIO Santander 2025. Contribuições são bem-vindas através de pull requests.

Licença
Este projeto é parte do Bootcamp DIO Santander e está disponível para fins educacionais.
