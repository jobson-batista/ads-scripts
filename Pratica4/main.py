from utils import utilizacao, tempo_de_resposta, carga_de_trabalho

# Modelo de Carga (Questão 2)
visitas_dict = {
    "home": 5,
    "search": 1.75,
    "add": 0.725,
    "pay": 0.29
}

f = open("output/carga_trab.txt","w")
f.write("Funcao Taxa_de_Chegada\n")

for item in visitas_dict:
    if(item == "home"):
        f.write("home 5\n")
    else:
        f.write(item + " " +str(carga_de_trabalho(5, visitas_dict[item]))+"\n")

f.close()
