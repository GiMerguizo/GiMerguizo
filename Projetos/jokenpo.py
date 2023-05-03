# Projeto desenvolvido no curso de Python - CursoemVídeo

from time import sleep
import emoji
import random
print('\033[31mDesafio 045\033[m')
print('-=' * 20)
print('\033[35mJokenpô\033[m')
print('-=' * 20)
lista = ['pedra', 'papel', 'tesoura']   # Tesoura = :v: ; Pedra = :punch: ; Papel = :hand:
pc = random.choice(lista)
'''itens = (Pedra, Papel, Tesoura)
computador = random.randint(0, 2)
pc = itens[computador]
print('O computador escolheu {}'.format(pc))'''
print('Vamos jogar Jokenpô!!')
a = str(input('O que você quer (pedra, papel ou tesoura)? ')).lower()
if pc == 'pedra':
    e = emoji.emojize(':punch:', use_aliases=True)
elif pc == 'papel':
    e = emoji.emojize(':hand:', use_aliases=True)
elif pc == 'tesoura':
    e = emoji.emojize(':v:', use_aliases=True)
else:
    e = emoji.emojize('')
print('PREPARAR!')
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('Eu escolho {} {}!'.format(pc, e))
if a == 'pedra' and pc == 'pedra':
    print('EMPATE!')
elif a == 'pedra' and pc == 'papel':
    print('UHUL! Eu ganhei!')
elif a == 'pedra' and pc == 'tesoura':
    print('AH NÃO! Eu perdi')
    print('Meus parabéns.')
elif a == 'papel' and pc == 'pedra':
    print('AH NÃO! Eu perdi')
    print('Meus parabéns.')
elif a == 'papel' and pc == 'papel':
    print('EMPATE!')
elif a == 'papel' and pc == 'tesoura':
    print('UHUL! EU ganhei!')
elif a == 'tesoura' and pc == 'pedra':
    print('UHUL! Eu ganhei!')
elif a == 'tesoura' and pc == 'papel':
    print('AH NÃO! Eu perdi')
    print('Meus parabéns.')
elif a == 'tesoura' and pc == 'tesoura':
    print('EMPATE!')
else:
    print('\033[31mEssa opção não é válida. Tente novamente.\033[m')
