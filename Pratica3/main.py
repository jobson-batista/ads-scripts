import os

output1 = 'output/questao1'
output2 = 'output/questao2'

# Executa 10 vezes cada algoritmo
def main():
    algs = ['quick','merge','counting']
    for k in range(10):
        for j in algs:
            os.system('java -cp bin MedidorDeOrdenacao ' + j + ' 10000000 1000000 | findstr /V "Algoritmo TamanhoDaEntrada ValorMaximo TempoDeOrdenacao">> ' + output1 + '/alg-' + j + '.txt')

# Executa um algoritmo específico, n vezes
def only_one(alg, n):
    for k in range(n):
        os.system('java -cp bin MedidorDeOrdenacao '+alg+' 10000000 1000000 | findstr /V "Algoritmo TamanhoDaEntrada ValorMaximo TempoDeOrdenacao">> ' + output1 + '/alg-' + alg +'-'+str(n)+'.txt')

# Executa cada algoritmo com cada valor de entrada (10M, 50M, 100M)
def letraA():
    algs = ['quick','merge','counting']
    inputs = [10000000, 50000000, 100000000]
    for k in inputs:
        for j in algs:
            os.system('java -cp bin MedidorDeOrdenacao ' + j +' '+ str(k) +' 1000000 | findstr /V "Algoritmo TamanhoDaEntrada ValorMaximo TempoDeOrdenacao">> ' + output2 + '/alg-'+j+'-questao2A.txt')

def letraB():
    algs = ['quick','merge','counting']
    inputs = [1000000, 10000000, 100000000]
    for k in inputs:
        for j in algs:
            os.system('java -cp bin MedidorDeOrdenacao ' + j +' 10000000 '+ str(k) +' | findstr /V "Algoritmo TamanhoDaEntrada ValorMaximo TempoDeOrdenacao">> ' + output2 + '/alg-'+j+'-questao2B.txt')


'''
main()
only_one('quick', 106)
only_one('merge', 106)
only_one('counting', 106)
'''

for a in range(5):
    # letraA()
    letraB()