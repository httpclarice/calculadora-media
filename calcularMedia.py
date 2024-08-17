def calcula_media(lista_de_notas):
 if len(lista_de_notas) == 0:
    return 0
 return sum(lista_de_notas)/len(lista_de_notas)

while True:
 classe_alunos = {}
 
 quantidade_de_alunos = int(input("Digite a quantidade de alunos na turma (2-7): "))
 
 for i in range(quantidade_de_alunos):
    nome = input(f'\n(Aluno {i + 1} de {quantidade_de_alunos}) Digite o nome do aluno: ')
    primeira_nota = float(input('... Digite a primeira nota (mínimo: 0 / máximo: 10): '))
    segunda_nota = float(input('... Digite a segunda nota (mínimo: 0 / máximo: 10): '))
    classe_alunos[nome] = {"notas": [primeira_nota,segunda_nota],"média": 
calcula_media([primeira_nota,segunda_nota])}
    
 medias = [aluno['média'] for aluno in classe_alunos.values()]
 print(f'\n\nMédia da turma: {calcula_media(medias):.2f}\nA turma 
tem{quantidade_de_alunos} alunos')
 
 media_max = max(medias)
 media_min = min(medias)
 for nome_aluno, dados in classe_alunos.items():
    if dados['média'] == media_max:
        print(f'A maior média foi do aluno {nome_aluno} com {media_max:.2f}')
    if dados['média'] == media_min:
        print(f'A menor média foi do aluno {nome_aluno} com {media_min:.2f}\n\n')
        
    sair_programa = input('Deseja que o programa seja executado novamente (SIM ou NÃO)? ')
 if sair_programa.upper() == 'SIM':
    print('\n\n=========\n')
 else:
    break