
from pathlib import Path

#caminho_pasta = Path.home() / 'W:/' / 'Shared With Me' / 'Clientes'/'Jettax'/'01 2024'/'NFS 01'/'NOTAS'/'JETTAX' #PASTA JETTAX

caminho_pasta = Path(r'C:\Users\jane\Desktop\notas') # Abre a Pasta
texto = (caminho_pasta.parts[-1])

#                                                                           Abre a Pasta 
arquivo = Path.home() / 'Desktop' / ('Pasta '+ texto + '.txt')


#                                                   Abre o arquivo (pega o var arquivo e abre usa o modo w tudo como f)
with arquivo.open(mode='w') as f:                   #O modo de escrita 'w' é utilizado para abrir um arquivo para escrita. Se o arquivo já existir, seu conteúdo será sobrescrito; se não existir, um novo arquivo será criado.
        for clientes in caminho_pasta.iterdir():
#                                                  o que tiver em clientes colocar no caminho_pasta escreve o primeiro nome do arquivo
            f.write(clientes.name + '\n')           # Loop escreva em F tudo que estiver em clientes e leia cada linha 
                                                    # o n É especialmente útil ao escrever múltiplas linhas para tornar o conteúdo mais legível e organizado

print('texto')


# Resumo do Roteiro: Criação de um Arquivo de Texto com Nomes de Arquivos

# Objetivo:
# Este script cria um arquivo de texto contendo os nomes dos arquivos presentes em uma determinada pasta.

# Passos:

# Importação de Bibliotecas: Importa a biblioteca pathlib.
# Definição do Caminho da Pasta: Especifica o caminho da pasta onde os arquivos estão localizados.
# Extração do Último Componente do Caminho: Obtém o último componente do caminho da pasta, que será usado no nome do arquivo de texto.
# Criação do Caminho do Arquivo de Texto: Cria o caminho do arquivo de texto usando o último componente do caminho da pasta.
# Abertura do Arquivo em Modo de Escrita: Abre o arquivo de texto em modo de escrita ('w').
# Iteração sobre os Arquivos na Pasta:
# Itera sobre os arquivos na pasta especificada.
# Escreve o nome de cada arquivo no arquivo de texto.
# Conclusão:
# Conclui a escrita no arquivo de texto.
# Saída:
# Imprime a palavra 'texto' (sem aspas). (Este print pode ser uma indicação de que o script foi concluído, mas parece um erro, já que deveria imprimir o conteúdo do arquivo, não a palavra 'texto'.)
# Este resumo explica de forma sucinta os passos realizados pelo script para criar um arquivo de texto com os nomes dos arquivos presentes em uma determinada pasta.
