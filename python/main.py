#!/bin/python3

import swordfish, os, sys

print("\n---> SWORDFISH v1.0 <---\n")

if "clear" in sys.argv:
    os.system('rm output/*')
    print("output/ limpo.")
else:
    pathFolder = str(input("Diretório com arquivos txt: "))
    swordfish.readAllFiles(pathFolder)
    swordfish.exportCSV()

