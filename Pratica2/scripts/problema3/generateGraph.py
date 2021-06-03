import matplotlib.pyplot as mtp
import sys

print(len(sys.argv))

if len(sys.argv) <= 1:
    print(
        "By neo - v1.0\n"\
        "Como usar:\n"\
        "   python3 generateGraph.py {arquivo-de-entrada} {nome-do-eixo-x} {nome-do-eixo-y}\n\n"\
        "   Ex: python3 generateGraph.py output/problema1-cm100.txt 'Taxa Chegada Média'  'Tempo Médio Resposta (s)'\n"
    )
else:
    problema2File = open(sys.argv[1],'r')
    data = problema2File.read().splitlines()
    del data[0]
    del data[-1]
    taxaChegadaMedia = []
    numServer = []
    tempoMedioResposta =[]

    for linha in data:
        # taxaChegadaMedia.append(int(linha.split(' ')[0].split('.')[0]))
        numServer.append(float(linha.split(' ')[2])) 
        tempoMedioResposta.append(float(linha.split(' ')[5]))

    problema2File.close()
    mtp.scatter(numServer, tempoMedioResposta)
    mtp.xlabel(sys.argv[2])
    mtp.ylabel(sys.argv[3])
    mtp.show()