def contar_votos():
    total_eleitores = int(input("Digite o número total de eleitores: "))
    
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    
    for eleitor in range(total_eleitores):
        voto = int(input(f"Eleitor {eleitor + 1}, vote (1, 2 ou 3): "))
        
        if voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1
        else:
            print("Voto inválido. Vote novamente.")
            continue
    
    print(f"Resultado da eleição:")
    print(f"Candidato 1: {candidato1} votos")
    print(f"Candidato 2: {candidato2} votos")
    print(f"Candidato 3: {candidato3} votos")

# Para testar:
# contar_votos()
