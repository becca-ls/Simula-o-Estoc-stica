arquivo = open('./Atividade_1./arquivo.txt', 'w')

frase = 'Esta eh um arquivo de exemplo.'
qtd = 20000000

for _ in range(qtd):
    arquivo.write(frase+'\n')

arquivo.close()

arquivo = open('./Atividade_1./arquivo.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
