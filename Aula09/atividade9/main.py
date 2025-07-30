from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Alexksandro', 20, '58865478425')

print(cliente1)

conta_do_alex = Conta(cliente1, 10.50, 1000)

print(conta_do_alex.cliente.nome, conta_do_alex.consulta_saldo())

conta_do_alex.depositar(1000.40)

print(conta_do_alex.consulta_saldo())

conta_do_alex.sacar(500)
print(conta_do_alex.consulta_saldo())

conta_do_alex.sacar(1000)
print(conta_do_alex.consulta_saldo())
