def utilizacao(taxa_chegada, demanda_servico):
    return taxa_chegada * demanda_servico

def tempo_de_resposta(demanda_servico, utilizacao):
    return demanda_servico/(1-utilizacao)

def carga_de_trabalho(quantidade_sesssoes, quantidade_visitas):
    return quantidade_sesssoes * quantidade_visitas

