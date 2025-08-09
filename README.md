# 💰 SISBANK - Sistema Bancário Simples em Python | Simple Banking System in Python

Este projeto é um sistema bancário básico desenvolvido em Python, com funcionalidades de depósito, saque e visualização de extrato. Ideal para fins educacionais e para praticar conceitos de orientação a objetos, validação de dados e interação com o usuário via terminal.

This project is a basic banking system developed in Python, featuring deposit, withdrawal, and statement viewing functionalities. It's ideal for educational purposes and practicing object-oriented programming, data validation, and terminal-based user interaction.

---

## 🚀 Funcionalidades | Features

- **Depósito | Deposit**: Permite ao usuário adicionar saldo à conta.  
  Allows the user to add funds to the account.

- **Saque | Withdrawal**: Permite realizar até 3 saques por dia, com validação de saldo e valor.  
  Allows up to 3 withdrawals per day, with balance and value validation.

- **Extrato | Statement**: Exibe o histórico de transações e o saldo atual.  
  Displays transaction history and current balance.

- **Interface via terminal | Terminal interface**: Menu interativo para facilitar o uso.  
  Interactive menu for easy usage.

---

## 🧠 Estrutura do Código | Code Structure

### Classe `SISBANK` | `SISBANK` Class

- `__init__(usuario)`: Inicializa o cliente com saldo zero, histórico vazio e contador de saques.  
  Initializes the client with zero balance, empty history, and withdrawal counter.

- `setDeposito(valor)`: Adiciona o valor ao saldo e registra no histórico.  
  Adds the value to the balance and logs it in the history.

- `setSaque(valor)`: Realiza saque com validações:  
  Performs withdrawal with validations:
  - Valor deve ser positivo | Value must be positive  
  - Valor não pode exceder o saldo | Value must not exceed balance  
  - Máximo de 3 saques por dia | Maximum of 3 withdrawals per day

- `getExtrato()`: Retorna o histórico de transações e o saldo final.  
  Returns transaction history and final balance.

### Interface Principal (`main`) | Main Interface

- Menu interativo com opções:  
  Interactive menu with options:
  - `[d]` Depositar | Deposit  
  - `[s]` Sacar | Withdraw  
  - `[e]` Extrato | Statement  
  - `[q]` Sair | Quit

- Validação de entrada com `try/except` para evitar erros de digitação.  
  Input validation using `try/except` to prevent typing errors.

---

## 📦 Como Executar | How to Run

1. Clone o repositório | Clone the repository:
   ```bash
   git clone https://github.com/seu-usuario/sisbank.git
   cd sisbank



   🛠️ Requisitos | Requirements
- Python 3.x
- Terminal ou IDE compatível com entrada de usuário
Terminal or IDE that supports user input


📚 Aprendizados | What You’ll Learn
Este projeto aborda  This project covers:
- Programação orientada a objetos  Object-oriented programming
- Encapsulamento de atributos  Attribute encapsulation
- Validação de dados  Data validation
- Interação com o usuário  User interaction
- Boas práticas de código limpo  Clean code practices


📌 Autor | Author
Desenvolvido por  Developed by Marco Aurélio
📍 Uberlândia, MG - Brasi
