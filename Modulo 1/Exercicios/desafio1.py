#Objetivo: Criar um programa que permita ao usuário adicionar, visualizar e marcar tarefas como concluídas.
#Descrição:
 #Você vai desenvolver um gerenciador de tarefas usando listas e dicionários. O programa deve:
#Permitir adicionar tarefas (com nome e descrição).
#Mostrar todas as tarefas não concluídas.
#Marcar tarefas como "concluídas" (alterando seu status).
#Opcional: Salvar as tarefas em um arquivo .txt para não perder ao fechar o programa.


tarefas = []

def adicionar():
    nome = input("digite qual tarefa voce vai fazer: ")
    descrição = input("descreva sua tarefa: ")
    status = input("a tarefa esta concluida? (sim/não) ")
   
    if status == "sim":
        concluida = True
    else:
        concluida = False
   
def visualisar():
    for t in tarefas:
        if t[2]:
            print(f"{t[0]} - {t[1]} concluida")
        else:
            print(f"{t[1]} - {t[0]} nao concluida")

mostrar = input("quer responder o questionario? (sim/nao): ")
if mostrar == "sim":
    adicionar()
    visualisar()
    
else:
     print("ok obrigado")

