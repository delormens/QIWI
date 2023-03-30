import pyqiwi
wallet = pyqiwi.Wallet(token='TOKEN QIWI', number='PHONE QIWI')
print(wallet.balance()) # выводит баланс кошелька
number = "" # номер куда перевести бабло
amount = 150 # сумма в рублях
comment = "сорри бро :( DELORMEN?" # комент к платежу
wallet.send(pid=99, recipient=number, amount=amount, comment=comment) # это сделает перевод