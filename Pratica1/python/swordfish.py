#!/bin/python3
import os
import pandas as aLib

def readAllFiles(folderInput):
    data = []
    # listando nome dos arquivos em diretorios.txt
    try:
        os.system('ls {path} > diretorios.txt'.format(path = folderInput))
        f1 = open('diretorios.txt','r')
        # ler cada linha de diretorios.txt
        for k in f1:
            # abrir cada arquivo k 
            f2 = open(folderInput + "/" + k.replace("\n",""),"r")
            firstLine = f2.readline().replace("\t",",")
            # add cada linha em data[]
            for k in f2:
                # Verifica se a linha k é igual a 
                # 'NumThreads   NumeroMaximo    StartTime   ElapsedTime MeanUtilization'
                # que no caso são as colunas
                if k != firstLine:
                    # Substitui o tab por ,
                    k = k.replace("\t",",")
                    # remoce ''
                    if k[-1] != '\n':
                        data.append(k+'\n')
                    else:
                        data.append(k)
        f2.close()
        f1.close()
        #os.system('rm diretorios.txt')

        data_sorted = sorted(data)
        f3 = open('output/result2.txt', 'w')
        f3.write(firstLine)
        for k in data_sorted:
            f3.write(k)
        f3.close()
        print("Pronto!\nResultado em {path}".format(path = "output/result.txt"))
    except IOError:
        print("Erro ao abrir arquivo!")
    except:
        print("Erro ao gerar txt!")

def exportCSV():
    try:
        result = aLib.read_csv('output/result2.txt')
        result.to_csv('output/result2.csv',index=None)
        print("Arquivo csv gerado!")
    except:
        print("Erro ao gerar arquivo csv.")
