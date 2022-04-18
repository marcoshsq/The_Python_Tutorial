# -*- coding: utf-8 -*-
"""01. An Informal Introduction to Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PqFpivxO2izMRWfd3SlOm2i8qB-6H1H_

# 03. An Informal Introduction to Python.

Essa é a parte 03 do tutorial oficial do Python, já que os primeiros dois capitulos falam apenas de como usar a linguagem através do Shell, eu não vou utiliza-la aqui, comecemos a partir do capítulo três.



1.   Números e operações básicas;
2.   Introdução á strings;
3.   Introdução as listas.
4.   Exercícios

[A página do tutorial](https://docs.python.org/3/tutorial/introduction.html)
"""

# Alguns comandos básicos do Python que são importantes:

"""O primeiro comando a aprender é o print(), a função print 
recebe algum objeto e imprime ele na tela ou no console."""

print("Oi, eu sou o computador!")

# Exercise 01

"""
Create your first program and help your computer greet the World.

"""


# Solution
from os import sep


print("Hello, World!")

# Other things we can do
print(
    "Hello", "World!", sep=","
)  # esse (sep="") separa as partes da string com o simbolo
print("Hello", "World", sep="**")
print("Hello", "World", sep="//")
print("Hello", end="*-*-*")  # o end coloca o seu conteúdo no final

# A função input() recebe dados do usuário:

# Exercício 02

"""
Ask the user for his name and give him a welcome message.
"""

# Solution
name = input("What's is your name? ")
print(f"Hi {name}, nice to meet you!")
print("Hi {}, nice to meet you!".format(name))
print("Hi", name + ", nice to meet you!")  # If we use the comma it will add a space
# But with the plus it concatenates!

"""# 3.1. Using Python as a Calculator

# 3.1.1. Números

Em Python os números são bastante diretos, os operadores são: soma (+), subtração (-), divisão (/), multiplicação (*), resto (%), divisão inteira (//) e potênciação (**)
"""

# Soma: 

1 + 1
5 + -1 # Não é necessário por parentêses no (-1).
       # O python já sabe que é um valor negativo.

# Subtração:

1 - 1
-5 - 9

# DIvisão:

10 / 5 # Divisão sempre retorna um Float
10 / 9

# Multiplicação:

5 * 0
10 * 110

# Resto:

10 % 7 # 10 dividido por 7 da um sobra, 3 logo essa operação dá 3
20 % 2 # Essa operação é útil para encontrar pares e ímpares
10 % 3 # Pois todo número par dividido por outro par dá resto 0

# Divisão inteira:

10 // 7 # 10 dividido por 7 da um sobra 3, logo essa operação dá 1

# Exp:

2 ** 2
2 ** 3

# A precedência de operadores é:
# parênteses, expoentes, multiplicação/divisão, adição/subtração

# Exercício 03

"""
Escreva um programa que leia um número e diga seu:

- Anterior e posterior;
- Dobro, triplo e raiz quadrada
"""

def operações(x):
    print(f"O número anterior é: {x - 1}")
    print(f"O número posterior é: {x + 1}")
    print(f"O dobro é: {x * 2}")
    print(f"O triplo é: {x * 3}")
    print(f"E sua raiz quadrada é: {x ** 0.5}")

operações(int(input("Insira um número:\n")))

"""# 3.1.2. Strings


"""

# String é texto, e no python não há diferença de string e char's
# Uma string de apenas 1 character é uma string pequenininha u.u

"Podemos declarar string com aspas duplas"
'Ou com aspas simples'
"Como a maioria dos textos são em inglês e usa-se muito o ', eu vou usar aspas duplas"

# existem operações que podem ser feitas com strings e a função print()
print("Por exemplo, colocar \ngera uma nova linha")
print("Na verdade o contra barra é um character especial")
# E dependendo com quem ele está, ele gera um comando diferente
# \n pula linha
# \a coloca um ponto na frase, tipo para lista

# Para evitar isso coloca-se um r antes das aspas, dizendo para o python que
# essa string é uma raw string u.u
print("O\n babaiaga")
print("O\a babaiaga")
print(r"O\n babaiaga")
print(r"O\a babaiaga")

# Existem outras formas de fazer um print que são muito hacker man!
print("Essa forma aqui, "
      "a frase ainda vai "
      "printada na mesma linha "
      r"caso eu não use \n por exemplo"

)

# Já usando aspas triplas é possível fazer uns print bem loko

print("""Oi abigos

    Me llamo Ramon Bolivar           +---+---+---+---+---+---+
                                     | P | y | t | h | o | n |
                                     +---+---+---+---+---+---+
                                     0   1   2   3   4   5   6
                                     -6  -5  -4  -3  -2  -1


	
(づ｡◕‿‿◕｡)づ: (◕‿◕) 		
                                                                (づ｡◕‿‿◕｡)づ: (◕‿◕)
(づ｡◕‿‿◕｡)づ: (◕‿◕)	
(づ｡◕‿‿◕｡)づ: (◕‿◕)
""")

# Dá para fazer concatenação de strings:

a = "Bola falando: "
b = "Karalho Zé... "
c = "Vai ser pai de novo..."
print(a + b + c) # Não se a diferença entre o mais e a virgula,
print(a, b, c)   # Mas, para concatenação, vou continuar usando o sinal de mais

# Também é possível multiplicar carácteres:

print("Oi " * 10)
print("-=-" * 25)

# String index:Strings podem ser indexadas (subscritos), 
# com o primeiro caractere tendo índice 0:

teste = "123456789"
teste[1]

# Os índices também podem ser números negativos, para começar a contar da direita:

teste[-1]

# Além da indexação, o fatiamento também é suportado. 
# Enquanto a indexação é usada para obter caracteres individuais, 
# o fatiamento permite obter a substring:

teste[1:5]

teste[:3] + teste[3:] # Observe como o início é sempre incluído e o fim sempre excluído. 
# Isso garante que s[:i] + s[i:] seja sempre igual a s:

# Strings são imutáveis, não é possível adicionar caracteres depois
# pra isso crie uma nova string u,u

# A função len da o tamanho de uma string:

nome = "Marcos"
len(nome)

"""# 3.1.3. Lists

Python conhece vários tipos de dados compostos, usados para agrupar outros valores. A mais versátil é a lista, que pode ser escrita como uma lista de valores separados por vírgulas (itens) entre colchetes. As listas podem conter itens de tipos diferentes, mas geralmente todos os itens têm o mesmo tipo.
"""

comidas = ["Arroz", "Feijão", "Frango", "Batata", "Ovos"]
comidas

# Assim como as strings (e todos os outros tipos de sequência integrados), 
# as listas podem ser indexadas e divididas: 

comidas[0] # Porém o índex retorna o item, não o caractere

comidas[2:4]

comidas[:3] + comidas[3:]

# Todas as operações de fatiamento retornam uma nova lista contendo os elementos solicitados. 
# Isso significa que a fatia a seguir retorna uma cópia superficial da lista:

comidas[:]

# listas aceitam concatenação:
comidas_update = comidas + ["Banana", "Linguiça", "Bacon"]

# listas podem ser modificadas:
# banana é uma fruta e batata um legume
comidas_update[3] = "Batata Frita"
comidas_update[5] = "Filé"
comidas_update

# O método append adiciona itens ao fim de uma lista:

comidas_update.append("Macarrão")

novo = input("Comida")
comidas_update.append(novo)
comidas_update

# É possível usar slices também para modificar vários itens de uma lista

comidas_update[:3] = []
comidas_update

# E para excluir a lista:

comidas_update [:] = []
comidas_update

# A função len também se aplica a listas:

num = [0, 1, 2, 3, 4, 5]
len(num) # retorna 6

# E é possível cirar lista dentro de listas, chamadas de listas 2D

num = [0, 1, 2, [3, 4, 5]]
len(num) # retorna 4

# para acessar os valores internos usamos [lista externa][lista interna]
num[3][2] # Para acessar o valor 5

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

# Um exemplo de algo legal que dá para se fazer com Python u.u

"""# Exercícios


"""