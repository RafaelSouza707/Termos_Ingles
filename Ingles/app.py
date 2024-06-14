import random
import ast
import os

def eliminaLinhas():
    print("\n" * os.get_terminal_size().lines)

# Carregar a lista de termos do arquivo termos.py
def loadDataSet():
    with open("termos.py", "r") as file:
        content = file.read()
        start = content.find('[')
        end = content.rfind(']') + 1
        lista_termos = ast.literal_eval(content[start:end])
        return lista_termos, content[:start], content[end:]

# Salvar a lista de termos no arquivo termos.py
def saveDataSet(lista_termos, prefix, suffix):
    with open("termos.py", "w") as file:
        file.write(prefix)
        file.write(str(lista_termos))
        file.write(suffix)
        
# Verificar se um termo já existe na lista de termos
def termoExiste(lista, termo):
    return any(item["termo"] == termo for item in lista)

# Inicializar lista_termos e tamLista
lista_termos, prefix, suffix = loadDataSet()
tamLista = len(lista_termos)

def aleatorizadorTermos():
    while True:
        random_word = random.randint(0, tamLista - 1)
        print_Termo = lista_termos[random_word]["termo"]
        resposta = lista_termos[random_word]["resposta"]
        print(print_Termo)

        answer = str(input("""
                            (Para voltar basta digitar 0)
                            Resposta: """))
        print()

        answer = answer.lower()
        resposta = resposta.lower()

        if answer == resposta:
            eliminaLinhas()
            print("Resposta Certa!")
            print()

        elif answer == "0":
            eliminaLinhas()
            menu()
            break

        else:
            eliminaLinhas()
            print("Resposta Errada!")
            print("A resposta correta é: ", resposta)
            print()

def printDataSet():
    for i in range(0, tamLista):
        print("ID: {} Termo: {} Resposta: {}".format(lista_termos[i]["id"], lista_termos[i]["termo"], lista_termos[i]["resposta"]))

def introduzirTermo():
    global lista_termos, tamLista
    print("Termos existentes:")
    printDataSet()
    
    answer = int(input("""
                    Deseja alterar ou adicionar um termo.
                    [1] - Adicionar termo.
                    [2] - Modificar termo.
                    [3] - Remover termo.
                    [4] - Para voltar.
                    """))

    if answer == 1:
        new_termo = str(input("Termo: "))
        new_resposta = str(input("Resposta do termo: "))
        
        if termoExiste(lista_termos, new_termo):
            print("O termo já existe na lista.")
        else:
            new_id = len(lista_termos)  # Novo ID baseado no tamanho da lista
            lista_termos.append({"id": new_id, "termo": new_termo, "resposta": new_resposta})
            tamLista = len(lista_termos)
            saveDataSet(lista_termos, prefix, suffix)
            print("Termo adicionado com sucesso.")
        
        eliminaLinhas()

        return introduzirTermo()
        
    elif answer == 2:
        termo_id = int(input("ID do termo a modificar: "))
        new_termo = str(input("Novo termo: "))
        new_resposta = str(input("Nova resposta do termo: "))

        for termo in lista_termos:
            if termo["id"] == termo_id:
                termo["termo"] = new_termo
                termo["resposta"] = new_resposta
                break
        
        saveDataSet(lista_termos, prefix, suffix)
        
        eliminaLinhas()
        printDataSet()

        return introduzirTermo()
        
    elif answer == 3:
        termo_id = int(input("ID do termo a remover: "))

        lista_termos = [termo for termo in lista_termos if termo["id"] != termo_id]
        tamLista = len(lista_termos)

        for i, termo in enumerate(lista_termos):
            termo["id"] = i
        
        saveDataSet(lista_termos, prefix, suffix)
        eliminaLinhas()
        printDataSet()

        return introduzirTermo()
    
    elif answer == 4:
        menu()
        
    else:
        print("Opção errada!")
        introduzirTermo()

def buscarTermo():
    termo_procurado = str(input("Qual o termo que deseja verificar? ")).lower()
    resultados = [termo for termo in lista_termos if termo_procurado in termo["termo"].lower()]
    
    if resultados:
        for termo in resultados:
            print("ID: {} Termo: {} Resposta: {}".format(termo["id"], termo["termo"], termo["resposta"]))
    else:
        print("Termo não encontrado.")
    
    return menu()

def menu():
    answer = int(input("""
                [1] - Iniciar aleatorizador de termos.
                [2] - Introduzir novo termo ou retirar termo.
                [3] - Verificar todos os termos
                [4] - Finalizar a aplicação.
                [5] - Buscar item.
                    """))
    
    if answer == 1:
        eliminaLinhas()
        aleatorizadorTermos()

    elif answer == 2:
        eliminaLinhas()
        introduzirTermo()

    elif answer == 3:
        eliminaLinhas()
        printDataSet()
        return menu()
    
    elif answer == 4:
        print("Aplicação finalizada.")
        return quit()
    
    elif answer == 5:
        eliminaLinhas()
        buscarTermo()

    else:
        eliminaLinhas()
        print("Opção inválida!")
        menu()

menu()
