
# -*- coding: utf-8 -*-

mensagem = "Hello World"
print(mensagem)

print ('Escolha a operação do banco de dados')
print ('1 - inserir')
print ('2 - ler')
print ('3 - atualizar')
print ('4 - deletar')

operacao = int(input('A operação é: '))

if operacao == 1:
    print ('inserir')

elif operacao == 2:
    print ('ler')
    pass

elif operacao == 3:
    print ('atualizar')
    pass

elif operacao == 4:
    print ('deletar')
    pass

else:
    print("nada a fazer")

print ("fim")
print ('A escolha é  {}!'.format(operacao))



