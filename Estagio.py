#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

print("Digite um número para verificar se ele pertence a sequência de Fibonacci: ")
n = int(input())

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
    if a == n:
        return True
    else:
        return False

if fibonacci(n):
    print("O número", n, "pertence a sequência de Fibonacci.")
else:
    print("O número", n, "não pertence a sequência de Fibonacci.")

#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

print("Digite uma palavra ou frase para verificar a quantidade de vezes que a letra 'a' aparece: ")
string = input()

def contar_a(string):
    return string.lower().count('a')

print("A letra 'a' aparece", contar_a(string), "vezes na palavra ou frase digitada.")

#3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA) #Resposta - 77

#4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, ___ 9
# b) 2, 4, 8, 16, 32, 64, ____ 128
# c) 0, 1, 4, 9, 16, 25, 36, ____ 49
# d) 4, 16, 36, 64, ____ 100
# e) 1, 1, 2, 3, 5, 8, ____ 13
# f) 2,10, 12, 16, 17, 18, 19, ____ não sei a resposta.

#5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

#Resposta: Ligue o primeiro interruptor e espere um tempo. Desligue o interruptor e ligue o segundo interruptor. Entre na sala. A lâmpada que estiver acesa é controlada pelo primeiro interruptor. A lâmpada que estiver apagada e quente é controlada pelo segundo interruptor. A lâmpada que estiver apagada e fria é controlada pelo terceiro interruptor.
