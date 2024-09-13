#	Ex1:
print('hello world')

#	Ex2
num = int(input('diga um numero: '))
print(f'o numero escolhido foi {num}')

#	Ex3
n1 = int(input('diga o primeiro numero: '))
n2 = int(input('diga o segundo numero: '))
print(f'a soma dos numeros {n1} e {n2} = {n1+n2}')

#	Ex4
nota1 = float(input("diga a nota: "))
nota2 = float(input("diga a nota: "))
nota3 = float(input("diga a nota: "))
nota4 = float(input("diga a nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'a média das notas é {media}')

#	Ex5
metros = int(input("diga a quantidade de metros: "))
centimetros = metros * 100
print(f'{metros}m equivale a {centimetros}cm')



#	Ex6
raio = int(input('diga o raio para calcular a área do seu circulo: '))
a = 3.14 * raio**2
print(f'a área do seu circulo é: {a}')

#	Ex7
l1 = int(input('diga o primeiro lado do seu quadrado: '))
l2 = int(input('diga o segundo lado do seu quadrado: '))
area = l1*l2
dobro = area*2
print(f'o seu lado 1 = {l1} e seu lado 2 = {l2}, e sua área é {area} e o dobro dela é {dobro}')

#	Ex8
salario = int(input('quanto você ganha por hora: '))
horas = int(input('e quantas horas você trabalha no mês: '))

salarioTotal = salario * horas
print(f'seu salário no mês é {salarioTotal}')

#	Ex9
f = int(input('diga a quantidade de graus F: '))
c = 5 * ((f-32) / 9)
print(f'convertendo: {f} graus Fahrenheit equivale a {c} graus celcius')




#	Ex10
c = int(input('diga a quantidade de graus C: '))
f = c * 1.8 + 32
print(f'convertendo: {c} graus celcius equivale a {f} graus Fahrenheit')

#	Ex11
n1 = int(input('diga o 1° numero: '))
n2 = int(input('diga o 2° numero: '))
dobroDoPrimeiro = n1*2
metadeDoSegundo = n2/2
n3 = dobroDoPrimeiro + metadeDoSegundo
somaDoTriplo = n1*3 + n3
n4 = n3**3

print(f'1° numero: {n1}')
print(f'2° numero: {n2}')
print(f'3° numero: {n3}')
print(f'4° numero: {n4}')

#	Ex12
altura = float(input("diga sua altura: "))
peso = (72.7 * altura) - 58
print(f'de acordo com a sua altura ({altura}), seu peso ideal é {peso}')





#	Ex13
sexo = input("você é homem ou mulher? digite \"h\" ou \"m\": ")

if sexo == 'h':
    altura_homem = float(input('digite sua altura homi: '))
    pesohomem = (72.7*altura_homem) - 58
    print(f'seu peso ideal é {pesohomem:.2f}')
else:
    altura_mulher = float(input('digite sua altura muie: '))
    pesomuie = (62.1*altura_mulher) - 44.7
    print(f'seu peso ideal é {pesomuie:.2f}')

#	Ex14
joaoPescador = int(input('quantos kilos joaoPescador trouxe (digite um numero inteiro): '))
if joaoPescador < 50:
    print('você não excedeu o limite de kilos')
else:
    excesso = joaoPescador - 50
    multa = excesso*4
    print(f'joao pescador terá que pagar R${multa} pois seu excesso foi de {excesso}kg')







#	Ex15
salario = int(input('quanto você ganha por hora: '))
horas = int(input('e quantas horas você trabalha no mês: '))

salarioBruto = salario * horas
print(f'seu salário no mês é {salarioBruto}')

renda = 0.11
inss = 0.08
sindico = 0.05

comRenda = salarioBruto * renda
comInss = salarioBruto * inss
comSindico = salarioBruto * sindico
todosImpostos = comSindico + comInss + comRenda
salarioLiquido = salarioBruto - todosImpostos

print(f'você tem o desconto de R${todosImpostos} e o seu salario liquido é R${salarioLiquido}')









#	Ex16
print("Bem-vindo à loja de tintas!")
print("Vamos calcular quanto você vai precisar de tinta e o custo total.")
area_str = input("Digite o tamanho da área a ser pintada em metros quadrados: ")

if area_str.replace('.', '', 1).isdigit() and area_str.count('.') <= 1:
    area = float(area_str)
    if area > 0:
        cobertura_por_litro = 3  # metros quadrados que 1 litro de tinta cobre
        litros_por_lata = 18  # litros por lata
        preco_por_lata = 80.00  # preço de cada lata

        litros_necessarios = area / cobertura_por_litro

        latas_necessarias = int(litros_necessarios / litros_por_lata)
        if litros_necessarios % litros_por_lata != 0:
            latas_necessarias += 1

        preco_total = latas_necessarias * preco_por_lata
        print(
            f"\nPara pintar uma área de {area:.2f} metros quadrados, você precisará de {latas_necessarias} lata(s) de tinta.")
        print(f"O custo total será de R$ {preco_total:.2f}.")
        print("Obrigado por usar nosso serviço!")
    else:
        print("A área deve ser um número positivo.")
else:
    print("Por favor, insira um número válido para a área.")
#	Ex17
print("Bem-vindo à loja de tintas!")
print("Vamos calcular quanto você vai precisar de tinta e o custo total.")
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
coberturaPorLitro = 6
litrosPorLata = 18
precoPorLata = 80.00
litrosPorGalao = 3.6
precoPorGalao = 25.00
litrosNecessarios = area / coberturaPorLitro
latasNecessarias = int(litrosNecessarios / litrosPorLata)
if litrosNecessarios % litrosPorLata != 0:
    latasNecessarias += 1

litrosRestantes = litrosNecessarios - (latasNecessarias * litrosPorLata)
galoesNecessarios = litrosRestantes * litrosPorGalao
if litrosRestantes % litrosPorGalao != 0:
    galoesNecessarios += 1
# Calcula o custo total
precoTotalLatas = latasNecessarias * precoPorLata
precoTotalGaloes = galoesNecessarios * precoPorGalao
precoTotal = precoTotalLatas + precoTotalGaloes

print(f"\nPara pintar uma área de {area:.2f} metros quadrados:")
print(f"Você precisará de {latasNecessarias} lata(s) de tinta.")
print(f"Você precisará de {galoesNecessarios} galão(ões) de tinta.")
print(f"O custo total será de R$ {precoTotal:.2f}.")
# Ex18
arquivo = float(input('Digite um tamanho de arquivo em MB: '))
velocidade = float(input('Digite a velocidade em Mbps(MB por segundos): '))

totalDeVelocidade = arquivo / velocidade
totalEmMinutos = totalDeVelocidade / 60

if totalEmMinutos != int(totalEmMinutos):
    totalEmMinutos = int(totalEmMinutos) + 1
else:
    totalEmMinutos = int(totalEmMinutos)
print(f'a velocidade de mb por minuto é de {totalEmMinutos:.2f}')

