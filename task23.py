class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner
        self.deposit()
        self.withdraw()
        self.get_balance()

    def deposit(self):  # Пополнение счета
        dep = input('Введите сумму пополнения: ')
        if self.balance == 0:
            self.balance += int(dep)
            print(f'Пополнение счета на {dep}')
        else:
            print("Счет заблокирован")

    def withdraw(self):  # Вывод средств
        dep = input('Введите сумму снятия: ')
        if self.balance > 0:
            self.balance -= int(dep)
            print(f'Снятие со счета на {dep}')
        else:
            print("Недостаточно средств")

    def get_balance(self):  # Получение баланса
        print(f'Баланс счета: {self.balance}')


while True:
    choise = input('Введите действие которые хотите сделать: Пополнить/Вывести/Посмотреть баланс:  ')
    tom = BankAccount(0, "Tom")
    if choise == 'Пополнить счет':
        tom.deposit()
    elif choise == 'Вывести баланс':
        tom.withdraw()
    elif choise == 'Посмотреть баланс':
        tom.get_balance()
    else:
        print('Вы ввели не верное действие')
    break
